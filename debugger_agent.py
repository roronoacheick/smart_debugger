from groq import Groq

def load_file(path: str) -> str:
    """
    Utility function to read a text file and return its content.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def call_groq_api(script_content: str, error_output: str) -> str:
    """
    Sends the script and its error to Groq LLM.
    Returns the raw JSON response as a string.
    """
    client = Groq()  

    system_prompt = load_file("prompt.txt")
    context = load_file("context.txt")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": context},
        {
            "role": "user",
            "content": (
                "Here is the Python script you must debug:\n\n"
                f"{script_content}\n\n"
                "Here is the error message:\n\n"
                f"{error_output}"
            )
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.1
    )

    return response.choices[0].message.content
