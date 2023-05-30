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

# Defining columns and adding descriptions
col1, col2 = st.columns(2)
with col1:
    st.subheader('Welcome to this page')
    st.write('This is a PoC for the project bla bla bla')

col1, col2 = st.columns(2)

with col1:
    st.image(img_fer)

with col2:
    st.subheader('Facial Emotion Recognition')
    st.write("The page 'Facial Emotion Recognition' allows stakeholders to interact with the fine-tuned model, thus observing how the model classifies images and webcam snapshots in real-time.")
    st.write("The page includes two tabs, namely 'Images' and 'Camera', in which emotions are classified and displayed along with the probability of each class labelling.")  


col1, col2 = st.columns(2)

with col1:
    st.subheader('MoodTrackr DEMO')
    st.write("MoodTrackr DEMO showcases the envisioned appearance of the dashboard which is to be presented to the end user when engaging with the product.")
    st.write("The dashboard presents three informative elements: Today’s Overall Mood, a sunburst graph displaying the composition and structure of websites used and the emotions classified, as well as metrics displaying whether a website has a positive or negative impact on user mental health.")

with col2:
    st.image(img_moodtrackr)