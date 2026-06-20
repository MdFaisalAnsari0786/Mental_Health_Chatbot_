import streamlit as st

from chatbot import get_response

st.set_page_config(
    page_title="Mental Health Companion",
    layout="wide"
)

st.title("Mental Health Companion Chatbot")

user_input = st.text_area(
    "How are you feeling today?"
)

if st.button("Send"):

    sentiment, response, tip = get_response(user_input)

    st.subheader("Detected Mood")

    st.success(sentiment.upper())

    st.subheader("Supportive Response")

    st.write(response)

    st.subheader("Relaxation Tip")

    st.info(tip)