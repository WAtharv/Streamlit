import streamlit as st
import pandas as pd
st.title("Streamlit Text input")

name=st.text_input("Enter your name")

age=st.slider("Select Your age:",0,100,25)

st.write(f"Your age is {age}.")


options=["Python","Java","C++","Javascript"]
choice=st.selectbox("Choose Your fav programming language",options)
st.write(f"You selected  {choice}.")

if name:
    st.write(f"Hello,{name}")

uploaded_file=st.file_uploader("Choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write