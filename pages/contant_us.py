import streamlit as st

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Your message here")
    button = st.form_submit_button("Submit")
    if button:
        print("I was pressed!")