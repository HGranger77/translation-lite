import streamlit as st
import requests
import yaml


# Load language code map from YAML file
with open("/app/languages_config.yaml", "r", encoding="utf-8") as f:
    language_code_map = yaml.safe_load(f)
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
