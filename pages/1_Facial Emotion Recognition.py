# Imports
import streamlit as st
from transformers import DeiTImageProcessor, DeiTForImageClassification
from PIL import Image
import requests
import torch
import matplotlib.pyplot as plt

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
    img_1_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_1.png', stream=True).raw)
    img_2_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_2.png', stream=True).raw)
    img_3_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_3.png', stream=True).raw)
    img_4_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_4.png', stream=True).raw)
    img_5_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_5.png', stream=True).raw)
    img_6_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_6.png', stream=True).raw)
    img_7_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_7.png', stream=True).raw)
    img_8_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_8.png', stream=True).raw)
    img_9_rd = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_9.png', stream=True).raw)

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
    option = st.selectbox('',('Image 1', 'Image 2', 'Image 3', 'Image 4', 'Image 5', 'Image 6', 'Image 7', 'Image 8', 'Image 9'))

    col1, col2 = st.columns(2)

    # Displaying the selected image in a larger format
    with col1:
    # Connecting the selected image to the same image in square format
        if option == 'Image 1':
            img_classification, logits_values = predict_class(img_1_sq)
            st.image(img_1_rd)
        if option == 'Image 2':
            img_classification, logits_values = predict_class(img_2_sq)
            st.image(img_2_rd)
        if option == 'Image 3':
            img_classification, logits_values = predict_class(img_3_sq)
            st.image(img_3_rd)
        if option == 'Image 4':
            img_classification, logits_values = predict_class(img_4_sq)
            st.image(img_4_rd)
        if option == 'Image 5':
            img_classification, logits_values = predict_class(img_5_sq)
            st.image(img_5_rd)
        if option == 'Image 6':
            img_classification, logits_values = predict_class(img_6_sq)
            st.image(img_6_rd)
        if option == 'Image 7':
            img_classification, logits_values = predict_class(img_7_sq)
            st.image(img_7_rd)
        if option == 'Image 8':
            img_classification, logits_values = predict_class(img_8_sq)
            st.image(img_8_rd)
        if option == 'Image 9':
            img_classification, logits_values = predict_class(img_9_sq)
            st.image(img_9_rd)

    # Displaying the logits_values of the different classes
    with col2:
        fig, ax = plt.subplots(figsize=(8, 10))
        bars = ax.barh(class_label, logits_values, height=0.1)

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        text_position = max(logits_values) + 0.05

        for i, bar in enumerate(bars):
            ax.text(text_position, bar.get_y() + bar.get_height() / 2,
                    f'{logits_values[i]*100:.2f}%', va='center', ha='right')

        plt.xticks([])

        st.pyplot(fig)

        col1, col2, col3 = st.columns([1, 1.5, 0.5])
        col1.write('')
        col2.metric(label='', value=img_classification, delta="Emotion", delta_color="off")
        col3.write('')









with tab2:
    col1, col2 = st.columns(2)

    with col1:
        img_file_buffer = st.camera_input("")

        if img_file_buffer is not None:
            # Read image file buffer as a PIL Image:
            img_camera = Image.open(img_file_buffer)
    
        if img_file_buffer is not None:
            cam_classification, logits_values = predict_class(img_camera)

    with col2:
        if img_file_buffer is None:
            st.write('')
        if img_file_buffer is not None:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            col2.metric(label='', value=cam_classification, delta="Emotion", delta_color="off")

if img_file_buffer is None:
    st.write('')
if img_file_buffer is not None:
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.barh(class_label, logits_values, height=0.1)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    text_position = max(logits_values) + 0.05  # Define the fixed position for the text

    for i, bar in enumerate(bars):
        ax.text(text_position, bar.get_y() + bar.get_height() / 2,
                f'{logits_values[i]*100:.2f}%', va='center', ha='right')

    plt.xticks([])  # Hide the x-axis tick labels

    # Display the plot using st.pyplot()
    st.pyplot(fig)