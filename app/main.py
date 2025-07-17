from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.genai_model import generate_summary

app = FastAPI()

class InputRequest(BaseModel):
    input_text: str

@app.post("/generate")
async def generate(input_data: InputRequest):
    result = generate_summary(input_data.input_text)
    return {"summary": result}