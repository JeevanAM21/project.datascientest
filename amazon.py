import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Amazon Prime Dashboard", layout="wide")

# Amazon background image
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapers.com/images/hd/amazon-prime-video-black-background-1920x1080.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# countries
countries = [
"India","United States","United Kingdom","Canada","Australia",
"Germany","France","Japan","South Korea","Brazil",
"Mexico","Italy","Spain","Netherlands","Sweden",
"Norway","Denmark","Switzerland","Singapore","Malaysia",
"Thailand","Indonesia","UAE","South Africa","Turkey"
]

# sample names
names = [
"Rahul Sharma","Amit Patel","Priya Singh","John Smith","Emma Brown",
"Akira Tanaka","Carlos Diaz","Maria Lopez","David Miller","Sarah Wilson",
"Daniel Lee","Sophia Garcia","James Anderson","Olivia Martin",
"Lucas Rossi","Liam Johnson","Noah Kim","Mia Chen","Arjun Reddy","Fatima Ali"
]

# generate dataset
data = []
years = list(range(2015,2026))
customer_id = 1000

for year in years:
    for i in range(200):
        customer_id += 1
        data.append([
            f"C{customer_id}",
            random.choice(names),
            random.choice(countries),
            year,
            random.choice(["Added","Cancelled"])
        ])

df = pd.DataFrame(data, columns=[
"Customer_ID","Customer_Name","Country","Year","Status"
])

st.title("Amazon Prime Customer Analytics (2015–2025)")

# filters
country = st.selectbox("Select Country", countries)
year = st.selectbox("Select Year", years)

filtered = df[(df["Country"]==country) & (df["Year"]==year)]

added = filtered[filtered["Status"]=="Added"].shape[0]
cancelled = filtered[filtered["Status"]=="Cancelled"].shape[0]

# metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Customers Added", added)

with col2:
    st.metric("Customers Cancelled", cancelled)

st.subheader("Customer Data")

st.dataframe(filtered)