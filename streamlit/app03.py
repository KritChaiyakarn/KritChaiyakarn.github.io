import streamlit as st

h = st.header('My Web Site')
s = st.subheader('เว็บไซต์ส่วนตัวของฉานน')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงือและความอดทน')
banner = st.image('https://picsum.photos/800/250')
b = st.button('click me')
text = st.text_input('promt: ')
if text:
    # text
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ. . .')