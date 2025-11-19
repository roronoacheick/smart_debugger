def _is_illegal_line(line: str) -> bool:
    """
    Detects suspicious or unwanted lines that the LLM might try to add.
    Prevents: debug messages, extra prints, comments, logging, etc.
    """
    forbidden_patterns = [
        "print(",
        "debug",
        "logging",
        "#",
    ]

    # Allow comments inside code blocks ONLY if originally present
    line_lower = line.lower()
    return any(p in line_lower for p in forbidden_patterns)


def apply_line_patch(file_path: str, line_number: int, fixed_line: str):
    
    if _is_illegal_line(fixed_line):
        raise ValueError(f"Suspicious single-line fix blocked: {fixed_line}")

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    index = line_number - 1

    if index < 0 or index >= len(lines):
        raise ValueError(f"Invalid line number: {line_number}")

    lines[index] = fixed_line.rstrip("\n") + "\n"

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def apply_block_patch(file_path: str, line_number: int, fixed_code: str):
    
    new_lines = [line + "\n" for line in fixed_code.split("\n")]

    for line in new_lines:
        if _is_illegal_line(line):
            raise ValueError(f"Suspicious line inside block fix: {line}")

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start_index = line_number - 1
    block_size = len(new_lines)

    if start_index < 0 or start_index >= len(lines):
        raise ValueError(f"Invalid line number: {line_number}")

    # Replace block of code
    lines[start_index:start_index + block_size] = new_lines

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
