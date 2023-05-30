# Imports
import streamlit as st
from PIL import Image
import requests

# Loading the images only once
@st.cache_resource
def read_objects():
    # Importing images
    img_fer = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_fer.png', stream=True).raw)
    img_moodtrackr = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_moodtrackr.png', stream=True).raw)

    return img_fer, img_moodtrackr

img_fer, img_moodtrackr = read_objects()

# Defining the columns and adding descriptions
col1, col2 = st.columns(2)

with col1:
    st.subheader('Facial Emotion Recognition')
    st.write('The page Facial Emotion Recognition allows stakeholders to interact with the fine-tuned model, thus observing how the model classifies images and webcam snapshots in real-time.')
    st.write('bla')  
    st.write('')  
    st.write('')  
    st.write('')  
    st.write('')  
    st.write('')  
    st.write('') 
    st.write('') 
    st.image(img_moodtrackr)

with col2:
    st.image(img_fer)
    st.subheader('MoodTrackr DEMO')
    st.write('bla')
    st.write('bla')
    st.write('bla')
    st.write('bla')  
