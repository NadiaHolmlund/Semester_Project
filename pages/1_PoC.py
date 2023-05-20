# PoC Streamlit application

# Imports
import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch
import numpy as np

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
    label2id = {label: id for id, label in id2label.items()}

    return processor, model, id2label, label2id


processor, model, id2label, label2id = read_objects()


# Defining a function to classify the image
def classify_image(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    #st.write("Predicted class:", id2label[predicted_class_idx])

    return predicted_class_idx


emotion_id = [0, 1, 2, 3, 4, 5, 6]
emotion_label = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']


tab1, tab2 = st.tabs(['Try stock images', 'Try yourself'])

with tab1:
    st.write("tab1")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        img_file_buffer = st.camera_input("Take a picture")

        if img_file_buffer is not None:
            # To read image file buffer as a PIL Image:
            img = Image.open(img_file_buffer)

            # To convert PIL Image to numpy array:
            img_array = np.array(img)   

            classification = classify_image(img) 
            classification_label = id2label[predicted_class_idx])

    with col2:
        if img_file_buffer is not None:
        #Anger = 
        #Disgust =
        #Fear =
        #Happiness =
        #Sadness =
        #Surprise =
        #Neutral =
            st.write(classification_label)

