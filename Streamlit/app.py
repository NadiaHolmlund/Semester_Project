# PoC Streamlit application

# Imports
import streamlit as st

# Setting up page configurations
st.set_page_config(
    page_title="Home",
    page_icon="💀",
    layout="wide")

st.title("Facial Emotion Recognition")

@st.cache
def load_model():

    save_dest = Path('model')
    save_dest.mkdir(exist_ok=True)
    
    f_checkpoint = Path("/content/gdrive/MyDrive/Semester_Project/mlruns/355554225098101950/71e8bc2658ca43339a0f42befc39de4f/artifacts/Model_experiment_1")

    if not f_checkpoint.exists():
        with st.spinner("Downloading model... this may take awhile! \n Don't stop it!"):
            from GD_download import download_file_from_google_drive
            download_file_from_google_drive(cloud_model_location, f_checkpoint)
    
    model = torch.load(f_checkpoint, map_location=device)
    model.eval()
    return model