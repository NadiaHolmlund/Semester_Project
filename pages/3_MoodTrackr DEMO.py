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
        counts = [10, 5, 7, 15, 8, 12, 20]  # Replace with your actual counts data

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

        # Set the smileys as annotations with adjusted font size
        fig.add_annotation(
            x=0.5,
            y=0.5,
            text=smileys[max_count_index],
            font={'size': 100},  # Adjust the font size for smileys
            showarrow=False,
        )


        # Display the chart
        st.plotly_chart(fig, use_container_width=True)




import plotly.graph_objects as go
import numpy as np

plot_bgcolor = "#def"
quadrant_colors = [plot_bgcolor, "#f25829", "#f2a529", "#eff229", "#85e043", "#2bad4e"]
quadrant_text = ["", "<b>Very high</b>", "<b>High</b>", "<b>Medium</b>", "<b>Low</b>", "<b>Very low</b>"]
n_quadrants = len(quadrant_colors) - 1

class_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
counts = [10, 5, 7, 15, 8, 12, 20]  # Replace with your actual counts data

# Find the index of the class with the highest count
max_count_index = counts.index(max(counts))

current_value = counts[max_count_index]
min_value = 0
max_value = max(counts)
hand_length = np.sqrt(2) / 4
hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))

fig = go.Figure(
    data=[
        go.Pie(
            values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),
            rotation=90,
            hole=0.5,
            marker_colors=quadrant_colors,
            text=quadrant_text,
            textinfo="text",
            hoverinfo="skip",
        ),
    ],
    layout=go.Layout(
        showlegend=False,
        margin=dict(b=0, t=10, l=10, r=10),
        width=450,
        height=450,
        paper_bgcolor=plot_bgcolor,
        annotations=[
            go.layout.Annotation(
                text=f"<b>IOT sensor value:</b><br>{current_value} units",
                x=0.5,
                xanchor="center",
                xref="paper",
                y=0.25,
                yanchor="bottom",
                yref="paper",
                showarrow=False,
            ),
            go.layout.Annotation(
                text=class_labels[max_count_index],
                x=0.5 + 0.25 * np.cos(hand_angle),
                xanchor="center",
                xref="paper",
                y=0.5 + 0.25 * np.sin(hand_angle),
                yanchor="middle",
                yref="paper",
                showarrow=False,
                font=dict(size=30),
            )
        ],
        shapes=[
            go.layout.Shape(
                type="circle",
                x0=0.48,
                x1=0.52,
                y0=0.48,
                y1=0.52,
                fillcolor="#333",
                line_color="#333",
            ),
            go.layout.Shape(
                type="line",
                x0=0.5,
                x1=0.5 + hand_length * np.cos(hand_angle),
                y0=0.5,
                y1=0.5 + hand_length * np.sin(hand_angle),
                line=dict(color="#333", width=4)
            )
        ]
    )
)

 # Display the chart
st.plotly_chart(fig, use_container_width=True)