from dotenv import load_dotenv
from google import genai
import os

# Step 1: Load API key
load_dotenv(override=True)

# Step 2: Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 3: Initialize Gemini
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What is Artificial Intelligence? Explain in simple words."
)
# Step 5: Display output
print("\nLLM Response:")
print(response.text)