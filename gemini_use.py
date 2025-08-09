import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_with_gemini(videos):
    """Summarize a list of YouTube videos using Gemini."""
    prompt = (
        "You are a marketing trend analyst.\n"
        "Here are YouTube search results:\n"
        f"{json.dumps(videos, indent=2)}\n"
        "Please summarize the main themes, patterns, and notable points "
        "in a concise, brand-relevant way for a brand team."
    )
    response = model.generate_content(prompt)
    return response.text