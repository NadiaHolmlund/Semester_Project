# Imports
import streamlit as st
from PIL import Image
import requests
from datetime import datetime
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Setting up page configurations
st.set_page_config(
    page_title="MoodTrackr",
    page_icon="😐",
    layout="wide")

# Setting the font size of metrics
st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 20px;
}
</style>
""",
    unsafe_allow_html=True,
)


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
    
    col1, col2 = st.columns(2)
    start_time = col1.text_input(label='Select Start Time', value='07:30')
    end_time = col2.text_input(label='Select End Time', value='16:30')

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

    # Filter the dataset based on the time_of_day column
    #timeframe_df = (avatar_df[avatar_df['time_of_day'].between(start_time, end_time)])

    timeframe_df = avatar_df[
        (avatar_df['time_of_day'] > start_time) &
        (avatar_df['time_of_day'] < end_time)
    ]

    if timeframe_df.empty:
        st.sidebar.error('ERROR: The timeframe you selected has no observations, please choose a broader timeframe')

    else:
        col1, col2 = st.columns(2)

        with col1:
            # Calculating the class_label with most counts and connecting it to the emoji
            emoji_counts = timeframe_df['class_label'].value_counts()
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
                            text=f"<b>Today\'s Overall<br>Mood</b><br><br>{max_count_emoji}",
                            x=0.5, xanchor="center", xref="paper",
                            y=0.4, yanchor="bottom", yref="paper",
                            showarrow=False)]))

            st.plotly_chart(fig, use_container_width=True)
        

        with col2:
            # Creating the figure
            fig = px.sunburst(
                data_frame=timeframe_df,
                path=['user_name', 'application_type', 'application', 'class_label'],
                values='application_duration_min',
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


        # Grouping the dataset by application and duration and identifying mode class_label
        grouped_df = timeframe_df.groupby('application').agg({'application_duration_min': 'sum', 'class_label': lambda x: x.mode()[0]}).reset_index().sort_values('application_duration_min', ascending=False)

        # Mapping class labels to text
        label_mapping = {
            'Anger': '-Increases Anger',
            'Disgust': '-Increases Disgust',
            'Fear': '-Increases Fear',
            'Happiness': 'Increases Happiness',
            'Sadness': '-Increases Sadness',
            'Surprise': 'Increases Surprise',
            'Neutral': 'Increases Neutral'}

        # Adding text to class_label values
        grouped_df['class_label'] = grouped_df['class_label'].apply(lambda x: label_mapping.get(x, x))

        # Displaying information in metrics
        col1, col2, col3, col4 = st.columns(4)

        if len(grouped_df) > 0:
            col1.metric(label="Duration: " + str(grouped_df.iloc[0]['application_duration_min']) + ' min.', value=str(grouped_df.iloc[0]['application']), delta=str(grouped_df.iloc[0]['class_label']))
        if len(grouped_df) > 1:
            col2.metric(label="Duration: " + str(grouped_df.iloc[1]['application_duration_min']) + ' min.', value=str(grouped_df.iloc[1]['application']), delta=str(grouped_df.iloc[1]['class_label']))
        if len(grouped_df) > 2:
            col3.metric(label="Duration: " + str(grouped_df.iloc[2]['application_duration_min']) + ' min.', value=str(grouped_df.iloc[2]['application']), delta=str(grouped_df.iloc[2]['class_label']))
        if len(grouped_df) > 3:
            col4.metric(label="Duration: " + str(grouped_df.iloc[3]['application_duration_min']) + ' min.', value=str(grouped_df.iloc[3]['application']), delta=str(grouped_df.iloc[3]['class_label']))
            