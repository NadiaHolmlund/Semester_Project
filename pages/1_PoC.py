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


        image_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_anger.jpg'

        response = requests.get(image_url)
        #image = Image.open(BytesIO(response.content))
                
        genre = st.radio(
        "Choose an image",
        ('Anger', 'Happiness', 'Sadness'))

    with col2:
        if genre == 'Anger':
            stock_classification = classify_image(img_anger)



col1, col2, col3 = st.columns(3)
col1.image(img_anger)
col2.image(img_happiness)
col3.image(img_sadness)


