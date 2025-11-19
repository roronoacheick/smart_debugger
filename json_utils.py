import json
import re

def extract_json(text: str) -> str:
    """
    Extract the first valid JSON object found in the text.
    This is necessary because LLMs may add text before or after the JSON.
    """
    # Regex to extract the first {...} block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM response.")
    return match.group(0)

def parse_llm_json(text: str) -> dict:
    """
    Clean and parse the JSON returned by the LLM.
    """
    json_str = extract_json(text)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON returned by LLM: {e}")

    return data
