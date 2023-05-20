# PoC Streamlit application

# Imports
import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch
import numpy as np
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

    img_angry = st.image('NadiaHolmlund/Semester_Project/pages/Streamlit_content/img_angry.jpg')
    img_sad = st.image('NadiaHolmlund/Semester_Project/pages/Streamlit_content/img_sad.jpg')
    img_happy = st.image('NadiaHolmlund/Semester_Project/pages/Streamlit_content/img_happy.jpg')

    return processor, model, emotion_id, emotion_label, id2label, img_angry, img_sad, img_happy


processor, model, emotion_id, emotion_label, id2label, img_angry, img_sad, img_happy = read_objects()








# Defining a function to classify the image
def classify_image(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    # Model predicts one of the 7 emotion classes
    predicted_class_id = logits.argmax(-1).item()
    predicted_class_label = id2label[predicted_class_id]

    return predicted_class_label











tab1, tab2 = st.tabs(['PoC on stock images', 'PoC on yourself'])






with tab1:
    col1, col2 = st.columns(2)

    with col1:
        

    with col1:
        st.write("hello")
















with tab2:
    col1, col2 = st.columns(2)

    with col1:
        img_file_buffer = st.camera_input("Take a picture")

        if img_file_buffer is not None:
            # Read image file buffer as a PIL Image:
            img = Image.open(img_file_buffer)
            
            # Apply classification model to the image
            classification = classify_image(img)










    with col2:
        st.write()'hello')
        #if img_file_buffer is not None:
            #logits = outputs.logits
            #labels = emotion_label

            #values = logits.tolist()[0]

            #plt.figure(figsize=(8, 6))
            #plt.barh(labels, values)
            #plt.xlabel('Logit Value')
            #plt.ylabel('Label')
            
            # Display the graph in Streamlit
            #st.pyplot(plt)

