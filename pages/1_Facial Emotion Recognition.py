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

    # Loading images with rounded edges
    img_1_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_1.jpg', stream=True).raw)
    img_2_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_2.jpg', stream=True).raw)
    img_3_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_3.jpg', stream=True).raw)
    img_4_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_4.jpg', stream=True).raw)
    img_5_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_5.jpg', stream=True).raw)
    img_6_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_6.jpg', stream=True).raw)
    img_7_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_7.jpg', stream=True).raw)
    img_8_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_8.jpg', stream=True).raw)
    img_9_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_9.jpg', stream=True).raw)

    # Loading images with square edges
    img_1_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_1.jpg', stream=True).raw)
    img_2_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_2.jpg', stream=True).raw)
    img_3_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_3.jpg', stream=True).raw)
    img_4_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_4.jpg', stream=True).raw)
    img_5_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_5.jpg', stream=True).raw)
    img_6_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_6.jpg', stream=True).raw)
    img_7_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_7.jpg', stream=True).raw)
    img_8_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_8.jpg', stream=True).raw)
    img_9_sq = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/square_images/img_9.jpg', stream=True).raw)

    return processor, model, class_id, class_label, id2label, img_1_rd, img_2_rd, img_3_rd, img_4_rd, img_5_rd, img_6_rd, img_7_rd, img_8_rd, img_9_rd, img_1_sq, img_2_sq, img_3_sq, img_4_sq, img_5_sq, img_6_sq, img_7_sq, img_8_sq, img_9_sq

processor, model, class_id, class_label, id2label, img_1_rd, img_2_rd, img_3_rd, img_4_rd, img_5_rd, img_6_rd, img_7_rd, img_8_rd, img_9_rd, img_1_sq, img_2_sq, img_3_sq, img_4_sq, img_5_sq, img_6_sq, img_7_sq, img_8_sq, img_9_sq = read_objects()


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
tab1, tab2 = st.tabs(['Images', 'Camera'])

# Setting up the tab for Images
with tab1:

    # Displaying the images
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
    
    col1.image(img_1_rd, 'Image 1')
    col2.image(img_2_rd, 'Image 2')
    col3.image(img_3_rd, 'Image 3')
    col4.image(img_4_rd, 'Image 4')
    col5.image(img_5_rd, 'Image 5')
    col6.image(img_6_rd, 'Image 6')
    col7.image(img_7_rd, 'Image 7')
    col8.image(img_8_rd, 'Image 8')
    col9.image(img_9_rd, 'Image 9')

    # Inserting a selectbox to select an image for classification
    option = st.selectbox('',('Select an image', 'Image 1', 'Image 2', 'Image 3'))
    st.write('')

    # Connecting the selected image to one in square format
    if option == 'Image 1':
        img_classification, logits_values = predict_class(img_1_sq)
        if option == 'Image 2':
        img_classification, logits_values = predict_class(img_2_sq)

    col1, col2 = st.columns(2)

    with col1:
        col1.image(img_1_rd)

