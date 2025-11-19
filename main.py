import subprocess
import sys
from pathlib import Path
from config import GROQ_API_KEY


def run_script(script_path: str):
    """
    Run a Python script in a separate process and return its output and error.

    script_path: path to the script you want to execute (ex: "bug.py")

    Returns:
        stdout (str): printed output from the script
        stderr (str): error message (if the script crashed)
        returncode (int): 0 means success, anything else means failure
    """
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


if __name__ == "__main__":
    main()
