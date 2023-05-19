# PoC Streamlit application

# Imports
import streamlit as st

pd.set_option("display.max_columns", None)

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide")

st.markdown("<h1 style='text-align: center; color: grey;'>Intelligent Scouting & Player Rating</h1>", unsafe_allow_html=True)