# main.py
import subprocess
import sys
from debugger_agent import call_groq_api
from json_utils import parse_llm_json
from patch_utils import apply_line_patch
from config import GROQ_API_KEY


def run_script(script_path: str):
    
    process = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )

    return process.stdout, process.stderr, process.returncode


def main():
    print("Smart debugger starting...")
    print("GROQ_API_KEY loaded:", bool(GROQ_API_KEY))

    script_path = "bug.py"

    # Step 1 : Execute the script
    stdout, stderr, code = run_script(script_path)

    print("\n=== STDOUT ===")
    print(stdout)

    print("\n=== STDERR ===")
    print(stderr)

    print("\n=== RETURN CODE ===")
    print(code)

    # If an error occurs → ask Groq for debugging help
    if code != 0:
        print("\nError detected → sending to Groq...\n")

        # Load the script content for the LLM
        with open(script_path, "r", encoding="utf-8") as f:
            script_content = f.read()

        # Step 2 : Ask Groq for debugging instructions
        llm_response = call_groq_api(script_content, stderr)

        print("=== LLM RAW RESPONSE ===")
        print(llm_response)

        # Step 3 : Parse the JSON returned by the LLM
        try:
            parsed = parse_llm_json(llm_response)
            print("\n=== PARSED JSON ===")
            print(parsed)

            # Step 4 : Apply in-place correction
            line_number = parsed.get("line_number")
            fixed_line = parsed.get("fixed_line")

            if line_number and fixed_line:
                apply_line_patch(script_path, line_number, fixed_line)
                print(f"\n✔ Patched line {line_number} in {script_path}")
            else:
                print("\n⚠️ No line_number or fixed_line provided by LLM.")

        except Exception as e:
            print("\n❌ Error parsing LLM JSON:", e)


if __name__ == "__main__":
    main()
