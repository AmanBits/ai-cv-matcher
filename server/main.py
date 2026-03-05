from fastapi import FastAPI, UploadFile, File, Form
import pdfplumber
import requests
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

API_KEY = os.getenv("OPENROUTER_API_KEY")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-cv-matcher.mhdaman828.workers.dev"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": "Bearer {API_KEY}",
    "Content-Type": "application/json"
}


@app.get("/")
def home():
    return {"message": "CV Matcher API Running"}


@app.post("/match-cv")
async def match_cv(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Extract text from PDF
    cv_text = ""

    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                cv_text += text + "\n"

    # Prompt for LLM
    prompt = f"""
You are an AI recruiter.

Match the following CV with the job description and give:

1. Match score (0-100)
2. Matching skills
3. Missing skills
4. Short explanation

CV:
{cv_text}

Job Description:
{job_description}
"""

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    result = response.json()
    
    ai_message = result["choices"][0]["message"]["content"]

    return {
        "filename": file.filename,
        "analysis": ai_message

    }



