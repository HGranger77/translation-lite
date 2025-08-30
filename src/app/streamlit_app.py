import streamlit as st
import requests


# Mapping of language names to their respective codes
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

# Streamlit app configuration
st.set_page_config(page_title="Translation Lite")
st.title("Translation Lite")

# Disable the app while the model is loading
with st.spinner("Initializing model..."):
    while True:
        try:
            response = requests.post("http://server:8000/infer", json={})
            break
        except requests.exceptions.RequestException:
            pass

# Input form
language = st.selectbox("Language", list(language_code_map.keys()), index=list(language_code_map.keys()).index("German"))
text_input = st.text_area("Translate:", height=200)

# Submit button
if st.button("Submit"):
    response = requests.post("http://server:8000/infer", json={"input_text": text_input, "language_code": language_code_map.get(language)})
    response.raise_for_status()
    translated_text = response.json().get("translated_text")
    st.text_area("Translation:", translated_text, height=200)
