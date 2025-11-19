def write_fixed_code(output_path: str, code: str):
   
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)

    return output_path
