from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pdf_reader import extract_text
from ai import answer_question
import os

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "data", "economics.pdf")
chapter_text = extract_text(PDF_PATH)

@app.post("/ask")
def ask(req: QuestionRequest):
    reply = answer_question(req.question, chapter_text)
    return {"teacher": reply}
