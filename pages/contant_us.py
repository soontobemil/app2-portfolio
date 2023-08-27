import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Your message here")
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)