import streamlit as st

# Setting up page configurations
st.set_page_config(
    page_title="MoodTrackr",
    page_icon="💀",
    layout="wide")

avatar = st.radio(
    "Pick your avatar:",
    ('Nadia', 'Nicklas', 'Nikolaj'))