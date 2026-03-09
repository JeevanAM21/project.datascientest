import streamlit as st
import pandas as pd

# Sample Data
data = {
    "Country": ["India","India","India","USA","USA","Japan"],
    "Status": ["Added","Cancelled","Added","Added","Cancelled","Added"]
}

df = pd.DataFrame(data)

st.title("Amazon Prime Customer Analysis")

# Country selection
country = st.selectbox("Select Country", df["Country"].unique())

# Filter data
filtered = df[df["Country"] == country]

# Count values
added = (filtered["Status"] == "Added").sum()
cancelled = (filtered["Status"] == "Cancelled").sum()

# Country flag images
flags = {
    "India":"https://flagcdn.com/w320/in.png",
    "USA":"https://flagcdn.com/w320/us.png",
    "Japan":"https://flagcdn.com/w320/jp.png"
}

flag_url = flags[country]

# Background flag display
st.markdown(f"""
<div style="
background-image: url('{flag_url}');
background-size: cover;
padding:40px;
border-radius:10px;
color:black;
font-size:22px;
font-weight:bold;
text-align:center;
">

<h2>{country} Customer Report</h2>

Customers Added: {added} <br><br>
Customers Cancelled: {cancelled}

</div>
""", unsafe_allow_html=True)