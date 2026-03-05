# AI CV Matcher

AI CV Matcher is a simple AI-powered web application that compares a candidate's CV with a job description and generates a **match score and analysis** using a Large Language Model.

The system extracts text from a **PDF CV**, sends it with the job description to an AI model, and returns insights such as matching skills, missing skills, and a compatibility score.

---

## Features

* Upload CV in **PDF format**
* Paste **job description**
* AI analyzes CV against the job description
* Generates **match score**
* Lists **matching skills**
* Lists **missing skills**
* Clean **mobile responsive UI**
* Loading indicator during AI processing

---

## Tech Stack

### Backend

* Python
* FastAPI
* pdfplumber (PDF text extraction)
* Requests (API calls)

### AI Model

* LLaMA 3 (via OpenRouter API)

### Frontend

* HTML
* CSS
* JavaScript
* Fetch API

---

## Project Structure

```
cv-matcher
│
├── main.py
├── index.html
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/cv-matcher.git
cd cv-matcher
```

### 2. Install dependencies

```
pip install fastapi uvicorn pdfplumber requests python-multipart
```

---

## Configure API Key

Replace the OpenRouter API key in `main.py`:

```
headers = {
    "Authorization": "Bearer YOUR_OPENROUTER_API_KEY",
    "Content-Type": "application/json"
}
```

You can get an API key from:
https://openrouter.ai

---

## Run the Server

```
uvicorn main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

---

## API Endpoint

### POST `/match-cv`

Uploads a CV and job description and returns the AI analysis.

**Request**

Form Data:

```
file: PDF CV
job_description: text
```

**Response Example**

```
{
  "filename": "cv.pdf",
  "analysis": "Match Score: 88..."
}
```

---

## Frontend

Open `index.html` in your browser.

The interface allows you to:

1. Upload your CV
2. Paste a job description
3. Click **Match CV**
4. View the AI analysis and score

---

## Example Output

```
Match Score: 88%

Matching Skills
- Java
- Spring Boot
- ReactJS

Missing Skills
- Microservices
- Banking domain knowledge
```

---

## Future Improvements

* Structured JSON output from AI
* Match score visualization
* Skill highlighting
* Batch CV matching
* Database integration
* Recruiter dashboard
* ATS-style filtering system

---

## License

This project is for educational and demonstration purposes.
