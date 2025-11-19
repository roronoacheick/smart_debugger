from config import GROQ_API_KEY

def main():
    # For now, just check that the config and API key work.
    print("Smart debugger starting...")
    print("GROQ_API_KEY loaded:", bool(GROQ_API_KEY))

if __name__ == "__main__":
    main()
