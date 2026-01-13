import streamlit as st

st.title("some basic commands")

name = st.text_input("enter your name")

if st.button("submit"):

    st.write(f"hello, {name}!")