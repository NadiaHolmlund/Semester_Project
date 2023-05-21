# Imports
import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification


# Setting up page configurations
st.set_page_config(
    page_title="Facial Emotion Recognition",
    page_icon="😐",
    layout="wide")

# Loading the processor, model and images only once
@st.experimental_singleton
def read_objects():
    # Importing the processor and model
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('NadiaHolmlund/Semester_Project', num_labels= 7, ignore_mismatched_sizes=True)
   
    # Defining the class idx and corresponding labels
    class_id = [0, 1, 2, 3, 4, 5, 6]
    class_label = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
    id2label = {id: label for id, label in zip(class_id, class_label)}

    return processor, model, class_id, class_label, id2label

processor, model, class_id, class_label, id2label = read_objects()

