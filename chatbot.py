import streamlit as st
import google.generativeai as genai
import os

GOOGLE_API_KEY = "AIzaSyCpjFcOYHzS_HR-gPW1M3OraEMTwevAFI4"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-pro")
chat = model.start_chat(history=[])

st.set_page_config(page_title="Simple ChatBot")
st.markdown("# 💬 Simple Chat Bot")
st.sidebar.markdown("## 🤖 Chat Bot Controls")

def get_gemini_response(query):
    response = chat.send_message(query, stream=True)
    return response

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Type your message:", key="input")
if st.button("Send") and input_text:
    st.session_state['chat_history'].append(("You", input_text))
    response = get_gemini_response(input_text)
    st.subheader("🤖 Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("📝 Chat History")
for role, message in st.session_state['chat_history']:
    st.write(f"**{role}**: {message}")
