import streamlit as st
import base64

# Function to set video background
def set_video_background(video_file):
    with open(video_file, "rb") as f:
        video_bytes = f.read()

    encoded_video = base64.b64encode(video_bytes).decode()

    video_html = f"""
    <style>
    .stApp {{
        position: relative;
        overflow: hidden;
    }}

    video {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        object-fit: cover;
    }}

    .content {{
        position: relative;
        z-index: 1;
        color: white;
        text-align: center;
    }}
    </style>

    <video autoplay muted loop>
        <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
    </video>
    """

    st.markdown(video_html, unsafe_allow_html=True)

# Set video background
set_video_background("amazon.mp4")

# Page Title
st.markdown("<h1 class='content'>Customer Churn Prediction</h1>", unsafe_allow_html=True)

# Description
st.markdown("""
<div class='content'>
<h3>Welcome to the Customer Churn Prediction App</h3>

This project predicts whether a customer will leave a company or stay.

Built using:
- Python
- Machine Learning
- Streamlit
</div>
""", unsafe_allow_html=True)