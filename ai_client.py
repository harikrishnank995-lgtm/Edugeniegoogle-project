import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def generate_text(prompt: str, *, json_mode: bool = False) -> str:
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "your_gemini_api_key_here":
        raise RuntimeError("GEMINI_API_KEY is missing. Copy .env.example to .env and add your Gemini API key.")
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    client = genai.Client(api_key=api_key)
    config = types.GenerateContentConfig(
        temperature=0.4,
        response_mime_type="application/json" if json_mode else "text/plain",
    )
    response = client.models.generate_content(model=model, contents=prompt, config=config)
    result = (response.text or "").strip()
    if not result:
        raise RuntimeError("Gemini returned an empty response. Please try again.")
    return result
