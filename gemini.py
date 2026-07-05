import os
from dotenv import load_dotenv
from personality import PERSONALITY

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from google import genai
      
client_ai = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt):
  response = client_ai.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
    {PERSONALITY}
    User: {prompt}
    """,
  )
  return response.text
