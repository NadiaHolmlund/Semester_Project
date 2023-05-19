# PoC Streamlit application

# Imports
import streamlit as st

pd.set_option("display.max_columns", None)

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide")

st.title("Hello")