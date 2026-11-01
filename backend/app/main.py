from fastapi import FastAPI
from pydantic import BaseModel
import sys, os

# This tells Python to look in the main folder for the 'core' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from core.parser import parse
from core.memory import judge, load_history

app = FastAPI()

class ScanRequest(BaseModel):
    text: str
    label: str = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(req: ScanRequest):
    rec = parse(req.text)
    history = load_history()
    verdict, reasons = judge(rec, history, req.label)
    return {"verdict": verdict, "reasons": reasons}
