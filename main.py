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
    print("Smart debugger starting…")
    print("GROQ_API_KEY loaded:", bool(GROQ_API_KEY))

    script_path = "bug.py"  # Script à corriger

    # Step 1 — Exécuter le script
    stdout, stderr, code = run_script(script_path)

    print("\n=== STDOUT ===")
    print(stdout)

    print("\n=== STDERR ===")
    print(stderr)

    print("\n=== RETURN CODE ===")
    print(code)

    # Si erreur → on appelle Groq
    if code != 0:
        print("\nError detected → sending to Groq…\n")

        # Charger le contenu du script pour le LLM
        with open(script_path, "r", encoding="utf-8") as f:
            script_content = f.read()

        # Step 2 — Appeler le LLM Groq
        llm_response = call_groq_api(script_content, stderr)

        print("=== LLM RAW RESPONSE ===")
        print(llm_response)

        # Step 3 — Parser le JSON du LLM
        try:
            parsed = parse_llm_json(llm_response)
            print("\n=== PARSED JSON ===")
            print(parsed)

            line_number = parsed.get("line_number")
            fixed_line = parsed.get("fixed_line")

            # On ignore fixed_code pour l'instant
            if line_number and fixed_line:
                apply_line_patch(script_path, line_number, fixed_line)
                print(f"\n✔ Single-line fix applied at line {line_number}")
            else:
                print("\n⚠️ No usable single-line fix found in LLM JSON.")

        except Exception as e:
            print("\n❌ Error while parsing or applying patch:", e)


if __name__ == "__main__":
    main()
