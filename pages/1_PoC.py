# PoC Streamlit application

# Imports
import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import torch
import matplotlib.pyplot as plt

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
    img_anger_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_anger.jpg'
    img_anger = Image.open(requests.get(img_anger_url, stream=True).raw)

    img_happiness_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_happiness.jpg'
    img_happiness = Image.open(requests.get(img_happiness_url, stream=True).raw)

    img_sadness_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_sadness.jpg'
    img_sadness = Image.open(requests.get(img_sadness_url, stream=True).raw)

    return processor, model, emotion_id, emotion_label, id2label, img_anger, img_happiness, img_sadness

processor, model, emotion_id, emotion_label, id2label, img_anger, img_happiness, img_sadness = read_objects()




# Defining a function to classify the image
def classify_image(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    # Model predicts one of the 7 emotion classes
    predicted_class_id = logits.argmax(-1).item()
    predicted_class_label = id2label[predicted_class_id]

    return predicted_class_label, logits.tolist()[0]





tab1, tab2 = st.tabs(['PoC on stock images', 'PoC on yourself'])





with tab1:
    col1, col2 = st.columns(2)

    with col1:                
        genre = st.radio(
        "Choose an image",
        ('Anger', 'Happiness', 'Sadness'))

    with col2:
        if genre == 'Anger':
            stock_classification, logits_values = classify_image(img_anger)
            st.metric(label='Emotion', value=stock_classification)
        if genre == 'Happiness':
            stock_classification, logits_values = classify_image(img_happiness)
            st.metric(label='Emotion', value=stock_classification)
        if genre == 'Sadness':
            stock_classification, logits_values = classify_image(img_sadness)
            st.metric(label='Emotion', value=stock_classification)

col1, col2, col3 = st.columns(3)
col1.image(img_anger)
col2.image(img_happiness)
col3.image(img_sadness)




import numpy as np
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(emotion_label, values, height=0.1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

text_position = max(values) + 0.05  # Define the fixed position for the text

for i, bar in enumerate(bars):
    ax.text(text_position, bar.get_y() + bar.get_height() / 2,
            f'{values[i]*100:.2f}%', va='center', ha='right')

plt.xticks([])  # Hide the x-axis tick labels

# Display the plot using st.pyplot()
st.pyplot(fig)
