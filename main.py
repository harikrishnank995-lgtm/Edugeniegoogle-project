from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from ai_client import generate_text
from explanation_module import explain_concept
from qna import answer_question
from quiz_module import create_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="EduGenie Learning Assistant", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

class TaskRequest(BaseModel):
    task: Literal["qa", "explain", "quiz", "summarize", "learn"]
    text: str = Field(min_length=1, max_length=20000)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})

@app.get("/health")
def health():
    return {"status": "ok", "app": "EduGenie"}

def run_task(task: str, text: str):
    try:
        if task == "qa": return {"task": task, "result": answer_question(text)}
        if task == "explain": return {"task": task, "result": explain_concept(text)}
        if task == "quiz": return {"task": task, "result": create_quiz(text)}
        if task == "summarize": return {"task": task, "result": summarize_text(text)}
        if task == "learn": return {"task": task, "result": recommend_learning_path(text)}
        raise HTTPException(status_code=400, detail="Unknown task")
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

@app.post("/api/task")
def api_task(payload: TaskRequest):
    return run_task(payload.task, payload.text.strip())

@app.post("/qa")
def qa(payload: TaskRequest): return run_task("qa", payload.text.strip())
@app.post("/explain")
def explain(payload: TaskRequest): return run_task("explain", payload.text.strip())
@app.post("/quiz")
def quiz(payload: TaskRequest): return run_task("quiz", payload.text.strip())
@app.post("/summarize")
def summarize(payload: TaskRequest): return run_task("summarize", payload.text.strip())
@app.post("/learn/recommendations")
def learn(payload: TaskRequest): return run_task("learn", payload.text.strip())
