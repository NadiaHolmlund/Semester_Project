# Imports
import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import torch

# Setting up page configurations
st.set_page_config(
    page_title="Facial Emotion Recognition",
    page_icon="😐",
    layout="wide")


# Loading the processor, model and images
@st.experimental_singleton
def read_objects():
    # Loading the processor and model
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('NadiaHolmlund/Semester_Project', num_labels= 7, ignore_mismatched_sizes=True)
   
    # Defining the class id and corresponding labels
    class_id = [0, 1, 2, 3, 4, 5, 6]
    class_label = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
    id2label = {id: label for id, label in zip(class_id, class_label)}

    # Loading images for PoC
    img_anger_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_anger.jpg'
    img_disgust_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_disgust.jpg'
    img_fear_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_fear.jpg'
    img_happiness_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_happiness.jpg'
    img_sadness_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_sadness.jpg'
    img_surprise_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_surprise.jpg'
    img_neutral_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_neutral.jpg'

    img_anger = Image.open(requests.get(img_anger_url, stream=True).raw)
    img_disgust = Image.open(requests.get(img_disgust_url, stream=True).raw)
    img_fear = Image.open(requests.get(img_fear_url, stream=True).raw)
    img_happiness = Image.open(requests.get(img_happiness_url, stream=True).raw)
    img_sadness = Image.open(requests.get(img_sadness_url, stream=True).raw)
    img_surprise = Image.open(requests.get(img_surprise_url, stream=True).raw)
    img_neutral = Image.open(requests.get(img_neutral_url, stream=True).raw)

    return processor, model, class_id, class_label, id2label, img_anger, img_disgust, img_fear, img_happiness, img_sadness, img_surprise, img_neutral

processor, model, class_id, class_label, id2label, img_anger, img_disgust, img_fear, img_happiness, img_sadness, img_surprise, img_neutral = read_objects()


# Defining a function to predict the class of emotion
def predict_class(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    # Model predicts one of the 7 classes of emotion
    predicted_class_id = logits.argmax(-1).item()
    predicted_class_label = id2label[predicted_class_id]

    return predicted_class_label, logits.tolist()[0]


# Setting up the page
tab1, tab2 = st.tabs(2)

with tab1:
    col1, col2, col3 = st.columns
    col1.img_anger
    col2.img_disgust
    col3.img_fear

    option = st.selectbox(
    'Select an image',
    ('Image 1', 'Image 2', 'Image 3'))

with tab2: 
    st.write('hello')