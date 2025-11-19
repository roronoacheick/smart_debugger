import subprocess
import sys
from pathlib import Path
from config import GROQ_API_KEY
from debugger_agent import call_groq_api  # NEW IMPORT


def run_script(script_path: str):
   
    process = subprocess.run(
        [sys.executable, script_path],  # run the script using the venv interpreter
        capture_output=True,            # capture stdout and stderr
        text=True                       # decode outputs as strings
    )

    return process.stdout, process.stderr, process.returncode


def main():
    print("Smart debugger starting...")
    print("GROQ_API_KEY loaded:", bool(GROQ_API_KEY))

    # For now, we test subprocess by running a purposely buggy script.
    script = "bug.py"

    # Run the script and capture its execution info
    stdout, stderr, code = run_script(script)

    print("\n=== STDOUT ===")
    print(stdout)

    print("\n=== STDERR ===")
    print(stderr)

    print("\n=== RETURN CODE ===")
    print(code)

    
    if code != 0:
        print("\nError detected → sending to Groq...\n")

        # Read the script content
        with open(script, "r", encoding="utf-8") as f:
            script_content = f.read()

        # Send script + error to Groq
        llm_response = call_groq_api(script_content, stderr)

        print("\n=== LLM JSON RESPONSE ===")
        print(llm_response)


if __name__ == "__main__":
    main()
