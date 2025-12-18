from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from pdf_reader import extract_text
from ai import answer_question

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "data", "economics.pdf")

@app.post("/ask")
def ask(req: QuestionRequest):
    try:
        chapter_text = extract_text(PDF_PATH)
        reply = answer_question(req.question, chapter_text)
        return {"teacher": reply}
    except Exception as e:
        return {"teacher": "Error processing the request"}
