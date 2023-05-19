# PoC Streamlit application

# Imports
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

pd.set_option("display.max_columns", None)

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide")

st.markdown("<h1 style='text-align: center; color: grey;'>Intelligent Scouting & Player Rating</h1>", unsafe_allow_html=True)
st.write('')

# Loading images and videos only once
@st.experimental_singleton
def read_objects():
    img_1 = Image.open('Images/Home_img_1.png')
    img_2 = Image.open('Images/Home_img_2.png')
    img_3 = Image.open('Images/Home_img_3.png')
    video_1 = open('Images/Home_vid_1.mov', 'rb')
    video_2 = open('Images/Home_vid_2.mov', 'rb')
    video_3 = open('Images/Home_vid_3.mov', 'rb')
    return img_1, img_2, img_3, video_1, video_2, video_3

img_1, img_2, img_3, video_1, video_2, video_3 = read_objects()