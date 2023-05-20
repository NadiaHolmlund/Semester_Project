# PoC Streamlit application

# Imports
import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch
#import matplotlib.pyplot as plt

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="💀",
    layout="wide")






# Loading processor, model, labels and images only once
@st.experimental_singleton
def read_objects():
    # Importing processor and model
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('NadiaHolmlund/Semester_Project', num_labels= 7, ignore_mismatched_sizes=True)
   
    # Creating labels
    emotion_id = [0, 1, 2, 3, 4, 5, 6]
    emotion_label = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
    id2label = {id: label for id, label in zip(emotion_id, emotion_label)}

    # Importing images
    img_angry = ('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_angry.jpg')
    img_happy = ('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_happy.jpg')
    img_sad = ('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_sad.jpg')

    return processor, model, emotion_id, emotion_label, id2label, img_angry, img_happy, img_sad

processor, model, emotion_id, emotion_label, id2label, img_angry, img_happy, img_sad = read_objects()






tab1, tab2 = st.tabs(['PoC on stock images', 'PoC on yourself'])





with tab1:
    col1, col2 = st.columns(2)

    with col1:
        genre = st.radio(
        "Choose an image",
        (img_angry, img_happy, img_sad))

    with col1:
        st.write("hello")