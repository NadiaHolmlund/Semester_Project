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

