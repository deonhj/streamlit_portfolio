import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="form"):
    user_email = st.text_input(label="Your email address")
    raw_message = st.text_area(label="Your message here")
    message = f"""\
Subject: Portfolio Website Query

Requestor: {user_email}

{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
