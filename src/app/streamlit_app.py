import streamlit as st
import requests


language_code_map = {
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Spanish": "spa_Latn",
    "Italian": "ita_Latn",
    "Chinese": "zho_Hans",
    "Russian": "rus_Cyrl",
    "Hindi": "hin_Deva",
    "Japanese": "jpn_Jpan",
    "Korean": "kor_Hang",
    "Portuguese": "por_Latn",
    "Dutch": "nld_Latn",
    "Swedish": "swe_Latn",
    "Turkish": "tur_Latn",
    "Vietnamese": "vie_Latn",
}
language_code_map = dict(sorted(language_code_map.items()))

st.set_page_config(page_title="Translation Lite")
st.title("Translation Lite")

with st.spinner("waiting"):
    while True:
        try:
            response = requests.post("http://server:8000/infer", json={})
            break
        except requests.exceptions.RequestException:
            pass

text_input = st.text_area("Translate:")
language = st.selectbox("Language", list(language_code_map.keys()))

if st.button("Submit"):
    response = requests.post("http://server:8000/infer", json={"input_text": text_input, "language_code": language_code_map.get(language)})
    response.raise_for_status()
    translated_text = response.json().get("translated_text")
    st.text_area("Translation:", translated_text)
