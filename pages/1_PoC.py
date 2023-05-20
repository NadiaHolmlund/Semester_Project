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






# Loading data, models, scalers, explainers, etc., only once
@st.experimental_singleton
def read_objects():
    # Importing processor and model
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('NadiaHolmlund/Semester_Project', num_labels= 7, ignore_mismatched_sizes=True)
   
    # Creating labels
    emotion_id = [0, 1, 2, 3, 4, 5, 6]
    emotion_label = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
    id2label = {id: label for id, label in zip(emotion_id, emotion_label)}

    return processor, model, emotion_id, emotion_label, id2label


processor, model, id2label = read_objects()




img_angry = st.image('NadiaHolmlund/Semester_Project/pages/Streamlit_content/img_angry.jpg')
img_sad = st.image('NadiaHolmlund/Semester_Project/pages/Streamlit_content/img_sad.jpg')
img_happy = st.image('NadiaHolmlund/Semester_Project/pages/Streamlit_content/img_happy.jpg')