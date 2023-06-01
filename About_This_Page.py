# Imports
import streamlit as st
from PIL import Image
import requests

# Loading the images only once
@st.cache_resource
def read_objects():
    # Importing images
    img_default = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_default.png', stream=True).raw)
    img_fer = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_fer.png', stream=True).raw)
    img_moodtrackr = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_moodtrackr.png', stream=True).raw)

    return img_default, img_fer, img_moodtrackr

img_default, img_fer, img_moodtrackr = read_objects()


# Defining the introduction columns
col1, col2 = st.columns(2)
with col1:
    st.subheader('Welcome!')
    st.write("This application showcases the product of the project. The application is divided into two sections, Facial Emotion Recognition and MoodTrackr DEMO, both of which showcase the capabilities of the fine-tuned vision transformer model on a proof-of-concept level.")


with col2:
    st.image(img_default)


# Defining the Facial Emotion Recognition columns
col1, col2 = st.columns(2)
with col1:
    st.image(img_fer)

with col2:
    st.subheader('Facial Emotion Recognition')
    st.write("The page 'Facial Emotion Recognition' allows stakeholders to interact with the fine-tuned model, thus observing how the model classifies images and webcam snapshots in real-time.")
    st.write("Explore the tabs on the page, Images and Camera, to test out the model!")


# Defining the MoodTrackr columns
col1, col2 = st.columns(2)
with col1:
    st.subheader('MoodTrackr DEMO')
    st.write("MoodTrackr DEMO showcases the envisioned appearance of the dashboard, which is presented to the end user when engaging with the product.")
    st.write("The dashboard presents three informative elements: Today’s Overall Mood, a sunburst graph of websites and emotions, as well as metrics displaying the impact of certain websites on user mental health.")

with col2:
    st.image(img_moodtrackr)