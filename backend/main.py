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

chapter_text = None  # cache

@app.post("/ask")
def ask(req: QuestionRequest):
    global chapter_text

    if chapter_text is None:
        chapter_text = extract_text(PDF_PATH)  # load once

    reply = answer_question(req.question, chapter_text)
    return {"teacher": reply}
