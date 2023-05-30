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

    start_time = st.time_input('Select Start Time', time(7, 30))
    end_time = st.time_input('Select End Time', time(16, 30))

    if start_time < end_time:
        pass
    else:
        st.error('Error: End time must be later than start time.')

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


    #selected_df = (avatar_df['time_of_day'] >= start_time) & (avatar_df['time_of_day'] <= end_time)


    col1, col2 = st.columns(2)

    with col1:
        fig = px.sunburst(data_frame=avatar_df,
                    path=['application_type', 'application', 'class_label'],
                    values='application_duration_min',
                    color='class_label',
                    hover_data={'class_label':False},)
        fig.update_layout(template="plotly_white", paper_bgcolor="#262730", margin=dict(t=20, b=20, l=30, r=30))

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        import plotly.graph_objects as go

        class_label = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
        smileys = ['😡', '🤢', '😨', '😄', '😢', '😮', '😐']
        counts = [10, 30, 7, 15, 8, 12, 20]  # Replace with your actual counts data

        # Find the index of the class with the highest count
        max_count_index = counts.index(max(counts))

        # Create the gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=max_count_index,
            gauge={
                'axis': {'range': [None, len(class_label) - 1], 'ticktext': smileys, 'tickvals': list(range(len(class_label)))},
                'bar': {'color': 'gray', 'thickness': 0.4},
                'steps': [
                    {'range': [0, len(class_label) - 1], 'color': 'lightgray'}
                ],
                'threshold': {
                    'line': {'color': 'red', 'width': 3},
                    'thickness': 0.75,
                    'value': max_count_index
                },
            },
        ))

        # Set the labels
        fig.update_layout(
            annotations=[
                dict(
                    x=0.5,
                    y=0.5,
                    text=class_label[max_count_index],
                    showarrow=False,
                    font=dict(size=40)  # Adjust the font size for smileys
                )
            ]
        )

        # Display the chart
        st.plotly_chart(fig, use_container_width=True)

