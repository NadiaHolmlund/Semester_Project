import streamlit as st

st.write("Main page giving a brief explanation of the project and the streamlit")
st.write("PoC illustrates that the model work and is able to make predictions")
st.write("application illustrates how the model would output would be applied on a user interface")

col1, col2 = st.columns(2)

with col1:
    st.header('Facial Emotion Recognition')
    st.write('bla')
    st.write('bla')

with col2:
    st.header('MoodTrackr DEMO')
    st.write('bla')
    st.write('bla')