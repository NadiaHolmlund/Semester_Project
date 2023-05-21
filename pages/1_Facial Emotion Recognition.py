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
    img_1_url = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_1.jpg'
    img_2 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_2.jpg'
    img_3 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_3.jpg'
    img_4 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_4.jpg'
    img_5 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_5.jpg'
    img_6 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_6.jpg'
    img_7 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_7.jpg'
    img_8 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_8.jpg'
    img_9 = 'https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/img_9.jpg'

    img_1 = Image.open(requests.get(img_1_url, stream=True).raw)
    img_2 = Image.open(requests.get(img_2, stream=True).raw)
    img_3 = Image.open(requests.get(img_3, stream=True).raw)
    img_4 = Image.open(requests.get(img_4, stream=True).raw)
    img_5 = Image.open(requests.get(img_5, stream=True).raw)
    img_6 = Image.open(requests.get(img_6, stream=True).raw)
    img_7 = Image.open(requests.get(img_7, stream=True).raw)
    img_8 = Image.open(requests.get(img_8, stream=True).raw)
    img_9 = Image.open(requests.get(img_9, stream=True).raw)

    return processor, model, class_id, class_label, id2label, img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8, img_9

processor, model, class_id, class_label, id2label, img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8, img_9 = read_objects()


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
col1, col2 = st.columns(2)

    # Visualzing the images on the page
with col1:
    col1, col2, col3 = st.columns(3)
    col1.image(img_1, 'Image 1')
    col2.image(img_2, 'Image 2')
    col3.image(img_3, 'Image 3')

    col1, col2, col3 = st.columns(3)
    col1.image(img_4, 'Image 4')
    col2.image(img_5, 'Image 5')
    col3.image(img_6, 'Image 6')

    col1, col2, col3 = st.columns(3)
    col1.image(img_7, 'Image 7')
    col2.image(img_8, 'Image 8') 
    col3.image(img_9, 'Image 9')
        
    # Adding a selectbox option to select which image to apply the model to
    option = st.selectbox('', ('Select an Image', 'Image 1',))
    if option == 'Image 1':
        selected_option = img_1

with col2:
    st.write('hello')
    #predicted_class, logits_values = predict_class(selected_option)
    #st.metric(label='Emotion', value=predicted_class)

# Setting up the tab for Camera
#with tab2:
#    st.write('hello')