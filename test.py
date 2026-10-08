from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

print("OpenAI API Key Loaded:", bool(openai_api_key))
print("Gemini API Key Loaded:", bool(gemini_api_key))