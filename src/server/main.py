from fastapi import FastAPI
from src.server.model import Model

app = FastAPI()
model = Model()

@app.post("/infer")
async def infer(request: dict):
    input_text = request.get("input_text")
    lid = request.get("lid")
    translated_text = model.infer(input_text, lid)
    return {"translated_text": translated_text}
