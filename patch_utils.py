def apply_line_patch(file_path: str, line_number: int, fixed_line: str):
   
    # Read all lines from file
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Convert human line number (1, 2, 3, ...) to Python index (0, 1, 2, ...)
    index = line_number - 1

    if index < 0 or index >= len(lines):
        raise ValueError(f"Invalid line number: {line_number}")

    # Replace the targeted line with the fixed one
    lines[index] = fixed_line.rstrip("\n") + "\n"

    # Write all lines back to the same file
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)