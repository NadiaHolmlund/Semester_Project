# PoC Streamlit application

# Imports
import streamlit as st

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="💀",
    layout="wide")

st.title("Facial Emotion Recognition")


from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests

url = 'https://c0.wallpaperflare.com/preview/990/418/320/adorable-black-and-white-black-and-white-boy.jpg'
image = Image.open(requests.get(url, stream=True).raw)
image

processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('/content/gdrive/MyDrive/Semester_Project/mlruns/355554225098101950/71e8bc2658ca43339a0f42befc39de4f/artifacts/Model_experiment_1', ignore_mismatched_sizes=True)

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits

# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])