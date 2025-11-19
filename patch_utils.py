def apply_line_patch(file_path: str, line_number: int, fixed_line: str):
    """
    Replace exactly one line in the file by a new corrected line.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Python lines start at index 0, but LLM returns lines starting at 1
    index = line_number - 1

    if index < 0 or index >= len(lines):
        raise ValueError(f"Invalid line number {line_number} for file {file_path}")

    # Replace the faulty line
    lines[index] = fixed_line.rstrip("\n") + "\n"

    # Write back the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
