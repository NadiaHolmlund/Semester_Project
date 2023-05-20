# PoC Streamlit application

# Imports
import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import torch

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="💀",
    layout="wide")

st.title("Facial Emotion Recognition")

url = 'https://c0.wallpaperflare.com/preview/990/418/320/adorable-black-and-white-black-and-white-boy.jpg'
image = Image.open(requests.get(url, stream=True).raw)

processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('NadiaHolmlund/Semester_Project', ignore_mismatched_sizes=True)