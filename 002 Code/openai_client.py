from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(prompt: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # 또는 gpt-4
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    content = response.choices[0].message.content

    if "피싱" in content:
        label = "피싱 가능성"
    elif "유해" in content:
        label = "유해 가능성"
    else:
        label = "정상"

    return {
        "label": label,
        "reason": content.strip()
    }