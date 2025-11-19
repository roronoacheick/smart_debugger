import os
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    # Small safety to help debugging if the key is missing
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")
