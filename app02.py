# streamlit run app02.py
import streamlit as st

st.title('OOP in ML')
st.sidebar.text('Sidebar')
st.sidebar.button('go>')
st.sidebar.button('went>')
st.sidebar.button('gone>')
st.image('./banner.jpg')
st.text_input('What your name?')