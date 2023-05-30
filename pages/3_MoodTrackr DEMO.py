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
        plot_bgcolor = "#262730"
        quadrant_colors = ["#0E1117"] * 8
        class_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
        smileys = ['😡', '🤢', '😨', '😄', '😢', '😮', '😐']

        current_value = 19
        min_value = 0
        max_value = 50
        hand_length = np.sqrt(2) / 7  # Adjust the hand length as desired
        hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))

        fig = go.Figure(
            data=[
                go.Pie(
                    values=[1 / 7] * 7,
                    rotation=90,
                    hole=0.5,
                    marker_colors=quadrant_colors,
                    text=smileys,
                    textinfo="text",
                    hoverinfo="skip",
                    textfont=dict(size=40)  # Adjust the text size as desired
                ),
            ],
            layout=go.Layout(
                showlegend=False,
                margin=dict(t=20, b=20, l=30, r=30),
                paper_bgcolor=plot_bgcolor,
                annotations=[
                    go.layout.Annotation(
                        text=f"<b>Today\'s Dominant<br>Mood</b>",
                        x=0.5, xanchor="center", xref="paper",
                        y=0.35, yanchor="bottom", yref="paper",
                        showarrow=False,
                    )
                ],
                shapes=[
                    go.layout.Shape(
                        type="circle",
                        x0=0.48, x1=0.52,
                        y0=0.48, y1=0.52,
                        fillcolor="#FAFAFA",
                        line_color="#FAFAFA",
                    ),
                    go.layout.Shape(
                        type="line",
                        x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                        y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                        line=dict(color="#FAFAFA", width=4)
                    )
                ]
            )
        )

        # Display the chart
        st.plotly_chart(fig, use_container_width=True)












import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

    # Calculate value counts for each emoji
    emoji_counts = avatar_df['class_emotion'].value_counts()

    # Determine emoji with maximum value count
    max_count_emoji = emoji_counts.idxmax()

    # Define the emoji and class labels
    smileys = ['😡', '🤢', '😨', '😄', '😢', '😮', '😐']
    class_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']

    # Find the index of the emoji with the maximum value count
    max_count_index = class_labels.index(max_count_emoji)

    # Update quadrant colors and arrow angle
    plot_bgcolor = "#262730"
    quadrant_colors = ["#0E1117"] * 7
    quadrant_colors[max_count_index] = "#FF0000"  # Replace with the desired color, e.g., red
    current_value = emoji_counts[max_count_emoji]
    min_value = 0
    max_value = avatar_df.shape[0]
    hand_length = np.sqrt(2) / 7
    hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))

    # Update text labels
    text_labels = [smileys[i] for i in range(len(smileys))]

    # Create the figure
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
                textfont=dict(size=40)
            ),
        ],
        layout=go.Layout(
            showlegend=False,
            margin=dict(t=20, b=20, l=30, r=30),
            paper_bgcolor=plot_bgcolor,
            annotations=[
                go.layout.Annotation(
                    text=f"<b>Today\'s Dominant<br>Mood</b>",
                    x=0.5, xanchor="center", xref="paper",
                    y=0.35, yanchor="bottom", yref="paper",
                    showarrow=False,
                )
            ],
            shapes=[
                go.layout.Shape(
                    type="circle",
                    x0=0.48, x1=0.52,
                    y0=0.48, y1=0.52,
                    fillcolor="#FAFAFA",
                    line_color="#FAFAFA",
                ),
                go.layout.Shape(
                    type="line",
                    x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                    y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                    line=dict(color="#FAFAFA", width=4)
                )
            ]
        )
    )

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
