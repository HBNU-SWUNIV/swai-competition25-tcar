from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai_client import ask_gpt
from prompt_generator import generate_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SiteData(BaseModel):
    url: str
    text: str

@app.post("/evaluate-site")
async def evaluate_site(data: SiteData):
    prompt = generate_prompt(data)
    result = ask_gpt(prompt)
    return result