from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = T5Tokenizer.from_pretrained("./artifacts")
model = T5ForConditionalGeneration.from_pretrained("./artifacts").to(device)

input_text = f"translate English to {lid}: {text}"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)

# Generate translation using beam search
outputs = model.generate(input_ids, num_beams=4, max_length=100, early_stopping=True)
translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
