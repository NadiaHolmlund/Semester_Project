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




col1, col2, col3, col4 = st.columns(4)

with col1:
    avatar = st.radio(
        "Pick your avatar:",
        ('Nadia', 'Nicklas', 'Nikolaj'))

with col2:
    st.image(img_nadia, caption='Nadia')

with col3:
    st.image(img_nicklas, caption='Nicklas')

with col4:
    st.image(img_nikolaj, caption='Nikolaj')