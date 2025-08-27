from fastapi import FastAPI
from model import Model


app = FastAPI()
model = Model()

@app.post("/infer")
async def infer(request: dict):
    input_text = request.get("input_text")
    language_code = request.get("language_code")
    translated_text = model.infer(input_text, language_code)
    return {"translated_text": translated_text}
