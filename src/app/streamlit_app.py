import streamlit as st
import requests

# Input text area
text_input = st.text_area("Translate:")
language = st.selectbox("Language", ('French', 'German', 'Spanish', 'Italian', 'Chinese'))

if st.button("Submit"):
    response = requests.post("http://localhost:8000/infer", json={"input_text": text_input, "language": language})
    response.raise_for_status()
    translated_text = response.json().get("translated_text")
    st.text_area("Translation:", translated_text)
