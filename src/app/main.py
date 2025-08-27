import streamlit as st
import requests

# Input text area
text_input = st.text_area("Translate:", height=150)
lid = st.selectbox("Language ID", ('fr', 'de', 'es', 'it', 'nl', 'pt', 'ru', 'zh'))

if st.button("Submit"):
    translated_text = infer(text_input, lid)
    st.text_area("Translation:", translated_text)

def infer(text, lid):
    response = requests.post("http://model:8501/infer", json={"text": text, "lid": lid})