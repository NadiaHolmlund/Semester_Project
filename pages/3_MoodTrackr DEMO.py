# Imports
import streamlit as st
from PIL import Image
import requests
from datetime import time
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

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

    #start_time = st.slider(label='Select Start Time', value=time(7, 30))
    #end_time = st.slider(label='Select End Time', value=time(16, 30))

    start_time = time(7, 30)
    end_time = time(16, 30)

    timeframe = st.slider(label='Select Timeframe', value=(start_time, end_time))

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


    col1, col2 = st.columns(2)

    with col1:
        # Calculating the class_label with most counts and connecting it to the emoji
        emoji_counts = avatar_df['class_label'].value_counts()
        max_count_emoji = emoji_counts.idxmax()
        class_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
        smileys = ['😡', '🤢', '😨', '😄', '😢', '😮', '😐']
        max_count_index = class_labels.index(max_count_emoji)

        # Updating plot colors
        plot_bgcolor = "#262730"
        quadrant_colors = ["#0E1117"] * 7
        quadrant_colors[max_count_index] = "#262730"

        # Updating text labels
        text_labels = [smileys[i] for i in range(len(smileys))]

        # Creating the figure
        fig = go.Figure(
            data=[
                go.Pie(
                    values=[1 / 7] * 7,
                    rotation=90,
                    hole=0.5,
                    marker_colors=quadrant_colors,
                    text=text_labels,
                    textinfo="text",
                    hoverinfo="skip",
                    textfont=dict(size=40))],
            layout=go.Layout(
                showlegend=False,
                margin=dict(t=20, b=20, l=30, r=30),
                paper_bgcolor=plot_bgcolor,
                annotations=[
                    go.layout.Annotation(
                        text=f"<b>Today\'s Dominant<br>Mood</b>",
                        x=0.5, xanchor="center", xref="paper",
                        y=0.45, yanchor="bottom", yref="paper",
                        showarrow=False)]))

        st.plotly_chart(fig, use_container_width=True)
    

    with col2:
        # Creating the figure
        fig = px.sunburst(
            data_frame=avatar_df,
            path=['user_name', 'application_type', 'application', 'class_label'],
            values='application_duration_min',
            #hover_data={'class_label': False},
            color_discrete_sequence=['#0E1117'],
            hover_data={'user_name':False,
                        'application_type':False,
                        'application':False,
                        'application_duration_min':False})

        # Updating plot layout
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#262730",
            margin=dict(t=20, b=20, l=30, r=30))

        st.plotly_chart(fig, use_container_width=True)



col1, col2 = st.columns(2)
col1.metric(label="Duration: 150 min.", value="TikTok", delta="Increases Happiness")
col2.write('')






# Create a dictionary to map the class labels
class_label_mapping = {
    'Anger': 'Negative',
    'Disgust': 'Negative',
    'Fear': 'Negative',
    'Sadness': 'Negative',
    'Happiness': 'Positive',
    'Surprise': 'Positive',
    'Neutral': 'Positive'
}

# Replace the emotion labels with the mapped values
avatar_df['mapped_class_label'] = avatar_df['class_label'].replace(class_label_mapping)

# Group by 'application' and count 'emotion_label' within each group
grouped_df = avatar_df.groupby('application')['mapped_class_label'].value_counts().reset_index(name='count')