import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeLine as DP

h = st.header('Diffusion.AI')
s = st.subheader('เว็บไซต์สำหรับแปลงข้อความเป็นภาพ')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงือและความอดทน')
text = st.text_input('promt: ')
if text:
    dp = DP.from_pretrained()
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ. . .')