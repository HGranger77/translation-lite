from src.server.model import Model

model = Model()
text = "Hello, how are you?"
languages = ["French", "German", "Spanish", "Italian", "Chinese"]

print("Test text:", text)
for language in languages:
    translated_text = model.infer(text, language)
    print(f"Translated text for {language}: {translated_text}")
