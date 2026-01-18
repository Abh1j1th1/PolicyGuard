from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

print("🔍 Checking available models for your API key...")
try:
    # In the new SDK, we just iterate and print the name
    for m in client.models.list():
        print(f"👉 Found: {m.name}")
except Exception as e:
    print(f"❌ Error: {e}")