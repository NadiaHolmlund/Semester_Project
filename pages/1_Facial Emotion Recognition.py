# Imports
import streamlit as st
from transformers import DeiTImageProcessor, DeiTForImageClassification
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
    processor = DeiTImageProcessor.from_pretrained('facebook/deit-base-distilled-patch16-224')
    model = DeiTForImageClassification.from_pretrained('NadiaHolmlund/Semester_Project', num_labels= 7, ignore_mismatched_sizes=True)
   
    # Defining the class id and corresponding labels
    class_id = [0, 1, 2, 3, 4, 5, 6]
    class_label = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
    id2label = {id: label for id, label in zip(class_id, class_label)}

    # Loading images with square edges
#    img_1_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_1.jpg'
#    img_2_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_2.jpg'
#    img_3_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_3.jpg'
#    img_4_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_4.jpg'
#    img_5_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_5.jpg'
#    img_6_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_6.jpg'
#    img_7_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_7.jpg'
#    img_8_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_8.jpg'
#    img_9_sqr_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_9.jpg'

    img_1_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_1.jpg', stream=True).raw)
#    img_2_sqr = Image.open(requests.get(img_2, stream=True).raw)
#    img_3_sqr = Image.open(requests.get(img_3, stream=True).raw)
#    img_4_sqr = Image.open(requests.get(img_4, stream=True).raw)
#    img_5_sqr = Image.open(requests.get(img_5, stream=True).raw)
#    img_6_sqr = Image.open(requests.get(img_6, stream=True).raw)
#    img_7_sqr = Image.open(requests.get(img_7, stream=True).raw)
#    img_8_sqr = Image.open(requests.get(img_8, stream=True).raw)
#    img_9_sqr = Image.open(requests.get(img_9, stream=True).raw)

    return processor, model, class_id, class_label, id2label, img_1_sq

processor, model, class_id, class_label, id2label, img_1_sq = read_objects()


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
#tab1, tab2 = st.tabs(['Images', 'Camera'])

# Setting up the tab for Images

#with tab1:
col1, col2, col3 = st.columns(3)

    # Visualzing the images on the page
with col2:
    col1, col2, col3 = st.columns(3)
    col1.image(img_1, 'Image 1')
