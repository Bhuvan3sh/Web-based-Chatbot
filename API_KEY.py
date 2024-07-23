import os
def save_api_key_to_env():
    api_key = input("Please enter your API key: ")

    with open(".env", "w") as env_file:
        env_file.write(f"API_KEY={api_key}\n")

    print("API key saved to .env file.")

def load_and_verify_api_key():
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv('API_KEY')
    if api_key:
        print(f"API key loaded successfully: {api_key}")
    else:
        print("Failed to load API key from .env file.")

save_api_key_to_env()
load_and_verify_api_key()

