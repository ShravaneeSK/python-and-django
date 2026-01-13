import streamlit as st

st.title("some basic commands like slider buttonsetc")

age = st.slider("select your age", 1, 100)
city = st.selectbox("select your city", ["pune", "mumbai", "bangalore", "chennai"])                
if st.button("show details"):
    st.write("age:", age)
    st.write("city:", city)