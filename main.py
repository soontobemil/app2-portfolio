import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jay Sim")
    content="I am a devops engineer"
    st.write(content)