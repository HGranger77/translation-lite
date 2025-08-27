from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class Model:
    def __init__(self, model_path="./artifacts"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(self.device)

    def get_lang_code(self, language):
        language_map = {
            "French": "fr",
            "German": "de",
            "Spanish": "es",
            "Italian": "it",
            "Chinese": "zh"
        }
        lang_code = language_map.get(language)
        if not lang_code:
            raise NotImplementedError(f"Unsupported language: {language}")
        lid_token = f"<{lang_code}>"
        lid_id = self.tokenizer.convert_tokens_to_ids(lid_token)
        return lid_id

    def infer(self, text, language):
        language_code = self.get_lang_code(language)
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        generated_tokens = self.model.generate(**inputs, forced_bos_token_id=language_code)
        translated_text = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return translated_text
