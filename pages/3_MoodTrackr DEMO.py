# Imports
import streamlit as st
from PIL import Image
import requests
from datetime import time
import plotly.express as px
import pandas as pd

# Setting up page configurations
st.set_page_config(
    page_title="MoodTrackr",
    page_icon="😐",
    layout="wide")

# Loading the datasets and images only once
@st.experimental_singleton
def read_objects():
    # Importing images
    img_nadia = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_1.png', stream=True).raw)
    img_nicklas = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_2.png', stream=True).raw)
    img_nikolaj = Image.open(requests.get('https://github.com/NadiaHolmlund/Semester_Project/raw/main/Streamlit_content/rounded_images/img_3.png', stream=True).raw)

    nadia_df = pd.read_csv('https://raw.githubusercontent.com/NadiaHolmlund/Semester_Project/main/Streamlit_content/avatars/nadia_df.csv')

    return img_nadia, img_nicklas, img_nikolaj, nadia_df

img_nadia, img_nicklas, img_nikolaj, nadia_df = read_objects()


with st.sidebar:
    col1, col2, col3 = st. columns(3)
    col1.image(img_nadia, caption='Nadia')
    col2.image(img_nicklas, caption='Nicklas')
    col3.image(img_nikolaj, caption='Nikolaj')

    avatar = st.selectbox(
        "Choose Your Avatar",
        ('Select', 'Nadia', 'Nicklas', 'Nikolaj'))
    
    timeframe = st.slider('Select a Timeframe', value=(time(7, 30), time(16, 30)))


if avatar == 'Select':
    st.header('Choose Your Avatar to interact with MoodTrackr DEMO')

else:    
    st.title("MoodTrackr")
    st.markdown('Hi ' + avatar +'! I\'m so glad to see you, let\'s have a look at how you\'re feeling today, shall we?')

    data = dict(
        character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
        value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

    fig = px.sunburst(
        data,
        names='character',
        parents='parent',
        values='value',
    )
    st.plotly_chart(fig)


    # Assuming you have the 'nadia_df' DataFrame with columns: 'application', 'application_type', 'application_duration_min'

    fig = go.Figure(go.Sunburst(
        labels=['GitHub', 'Google Colab', 'ChatGPT', 'Google Colab', 'Stack Overflow', 'Facebook', 'TikTok'],
        parents=['', 'Coding Notebook', 'AI Chatbot', 'Coding Notebook', 'Programming Q&A', 'Social Media', 'Social Media'],
        values=[30, 45, 15, 15, 15, 90, 150],
    ))
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    st.plotly_chart(fig)


