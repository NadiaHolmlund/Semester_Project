import streamlit as st

# Setting up page configurations
st.set_page_config(
    page_title="MoodTrackr",
    page_icon="💀",
    layout="wide")

avatar = st.radio(
    "Pick your avatar:",
    ('Nadia', 'Nicklas', 'Nikolaj'))


from PIL import Image

image = Image.open('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_anger.jpg')

st.image(image, caption='Sunrise by the mountains')