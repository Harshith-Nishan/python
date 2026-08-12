# import streamlit as st

# st.title("My First Streamlit App")

# st.write("Hello!")

import streamlit as st

st.title("My First GUI")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.write("Hello", name)