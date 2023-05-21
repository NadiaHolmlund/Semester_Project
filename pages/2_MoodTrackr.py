import streamlit as st
from PIL import Image
import requests

# Setting up page configurations
st.set_page_config(
    page_title="MoodTrackr",
    page_icon="💀",
    layout="wide")



# Loading processor, model, labels and images only once
@st.experimental_singleton
def read_objects():
    # Importing images
    nadia_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_anger.jpg'
    img_nadia = Image.open(requests.get(nadia_url, stream=True).raw)

    nicklas_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_happiness.jpg'
    img_nicklas = Image.open(requests.get(nicklas_url, stream=True).raw)

    nikolaj_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_sadness.jpg'
    img_nikolaj = Image.open(requests.get(nikolaj_url, stream=True).raw)

    return img_nadia, img_nicklas, img_nikolaj

img_nadia, img_nicklas, img_nikolaj = read_objects()



with st.sidebar:
    avatar = st.radio(
        "Choose Your Avatar:",
        ('Nadia', 'Nicklas', 'Nikolaj'))

    st.image(img_nadia, caption='Nadia')
    st.image(img_nicklas, caption='Nicklas')
    st.image(img_nikolaj, caption='Nikolaj')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import time

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)