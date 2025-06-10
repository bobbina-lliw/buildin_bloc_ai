import streamlit as st
import pandas as pd
import numpy as np

st.markdown(
    body = '''
    :red[Streamlit] :orange[can]
    '''
)
st.markdown(
    body="Thisthing; &mdash;\
        :tulip:"
)

image = ["yang.jpg","noraj.jpg"]
for img in image:
    st.image(img,width=300)

code = """
def hello():
    print("Gello Burld")
"""
st.code(
    body=code,
    language="python",
    line_numbers=True
)


st.write("dfgdfg, *World!* :sunglasses:")
#bot
st.title("Tuto bot")
if("Chat_history" not in st.session_state):
    st.session_state.chat_history = [
        "ai","hi im ai ask me shit"
    ]
#broken down
for role,message in st.session_state.chat_history:
    st.chat_message


user_input = st.chat_input(
    placeholder="type your message...",
    key = "user input"
)

if(user_input):
    st.chat_message("user").write(user_input)
