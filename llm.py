import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def summarize(text):
    if len(text.strip()) == 0:
        return ""

    msg = "Give sentiment (positive/negative/neutral) and a single sentence summary:\n\n" + text

    for attempt in range(3):
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": msg}],
                max_tokens=150
            )
            return res.choices[0].message.content.strip()
        except:
            time.sleep(3)
            
    return "Error getting summary"
