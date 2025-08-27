from fastapi import FastAPI
from src.server.model import Model

app = FastAPI()
model = Model()

@app.post("/infer")
async def infer(request: dict):
    input_text = request.get("input_text")
    language = request.get("language")
    translated_text = model.infer(input_text, language)
    return {"translated_text": translated_text}
