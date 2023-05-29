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
@st.cache_resource
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
    
    #timeframe = st.slider('Select a Timeframe', value=((7, 30), (16, 30)))

    start_time, end_time = st.slider('start time  - end time :', [])



if avatar == 'Select':
    st.header('Choose Your Avatar to interact with MoodTrackr DEMO')

else:    
    st.title("MoodTrackr")
    st.markdown('Hi ' + avatar +'! I\'m so glad to see you, let\'s have a look at how you\'re feeling today, shall we?')

    if avatar == 'Nadia':
        avatar_df = nadia_df
    if avatar == 'Nicklas':
        avatar_df = nicklas_df
    if avatar == 'Nikolaj':
        avatar_df = nikolaj_df
    
    #time_df = avatar_df[(avatar_df['time_of_day'] >= start_time) & (avatar_df['time_of_day'] <= end_time)]
    time_df = (selected_df['CREATEDDATE'] > start_date) & (selected_df['CREATEDDATE'] <= end_date)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.sunburst(data_frame=time_df,
                    path=['application_type', 'application', 'class_label'],
                    values='application_duration_min',
                    color='class_label',
                    hover_data={'class_label':False})
        st.plotly_chart(fig)

    with col2:
        st.write('')
        #st.metric(label="Application", value=selected_df[], delta="1.2 °F")
