# PoC Streamlit application

# Imports
import streamlit as st

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="💀",
    layout="wide")

st.title("Facial Emotion Recognition")

# Loading images and videos only once
#@st.experimental_singleton
#def read_objects():

#    return 

# = read_objects()