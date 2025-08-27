from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "t5-small"
save_directory = "./artifacts"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)
