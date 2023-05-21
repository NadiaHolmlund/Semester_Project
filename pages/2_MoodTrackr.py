import streamlit as st
from PIL import Image
import requests
from datetime import time

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
    col1, col2, col3 = st. columns(3)
    col1.image(img_nadia, caption='Nadia')
    col2.image(img_nicklas, caption='Nicklas')
    col3.image(img_nikolaj, caption='Nikolaj')

    avatar = st.selectbox(
        "Choose Your Avatar",
        ('Select', 'Nadia', 'Nicklas', 'Nikolaj'))
    
    timeframe = st.slider('Select a Timeframe', value=(time(7, 30), time(16, 30)))


if avatar == 'Select':
    st.write('')

else:    
    st.title("MoodTrackr")
    st.subtitle('Hi ' + avatar +'! I\'m so glad to see you, let\' have a look you are feeling today, shall we?')