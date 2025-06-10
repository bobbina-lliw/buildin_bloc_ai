from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import numpy as np
import os
import google.genai as genai

load_dotenv()

gapi_key = os.getenv("API_KEY")
client = genai.Client(api_key = gapi_key)

st.subheader("Poorly Generated AI")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ["ai", "hello! im your ai tutor, ask me anything you like"]
    ]

for role, msg in st.session_state.chat_history:
    st.chat_message(role).markdown(msg)

user_input = st.chat_input(
    placeholder="type a message...",
    key="user_input"
)

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(["user", user_input])
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=genai.types.GenerateContentConfig(
            system_instruction="speak like a normal person"
        ),
        contents=st.session_state.chat_history
    )
    ml_response = response.text
    st.chat_message("ai").write(ml_response)
    st.session_state.chat_history.append(["ai", ml_response])
