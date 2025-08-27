from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

class Model:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = T5Tokenizer.from_pretrained("./artifacts")
        self.model = T5ForConditionalGeneration.from_pretrained("./artifacts").to(self.device)

    def infer(self, text, lid):
         input_text = f"translate English to {lid}: {text}"
         input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to(self.device)

         # Generate translation using beam search
         outputs = self.model.generate(input_ids, num_beams=4, max_length=100, early_stopping=True)
         translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
         return translated_text
