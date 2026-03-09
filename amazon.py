import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Prime Customer Dashboard", layout="wide")

# 25 countries
countries = [
"India","United States","United Kingdom","Canada","Australia",
"Germany","France","Japan","South Korea","Brazil",
"Mexico","Italy","Spain","Netherlands","Sweden",
"Norway","Denmark","Switzerland","Singapore","Malaysia",
"Thailand","Indonesia","UAE","South Africa","Turkey"
]

# country flags
flags = {
"India":"https://flagcdn.com/w320/in.png",
"United States":"https://flagcdn.com/w320/us.png",
"United Kingdom":"https://flagcdn.com/w320/gb.png",
"Canada":"https://flagcdn.com/w320/ca.png",
"Australia":"https://flagcdn.com/w320/au.png",
"Germany":"https://flagcdn.com/w320/de.png",
"France":"https://flagcdn.com/w320/fr.png",
"Japan":"https://flagcdn.com/w320/jp.png",
"South Korea":"https://flagcdn.com/w320/kr.png",
"Brazil":"https://flagcdn.com/w320/br.png",
"Mexico":"https://flagcdn.com/w320/mx.png",
"Italy":"https://flagcdn.com/w320/it.png",
"Spain":"https://flagcdn.com/w320/es.png",
"Netherlands":"https://flagcdn.com/w320/nl.png",
"Sweden":"https://flagcdn.com/w320/se.png",
"Norway":"https://flagcdn.com/w320/no.png",
"Denmark":"https://flagcdn.com/w320/dk.png",
"Switzerland":"https://flagcdn.com/w320/ch.png",
"Singapore":"https://flagcdn.com/w320/sg.png",
"Malaysia":"https://flagcdn.com/w320/my.png",
"Thailand":"https://flagcdn.com/w320/th.png",
"Indonesia":"https://flagcdn.com/w320/id.png",
"UAE":"https://flagcdn.com/w320/ae.png",
"South Africa":"https://flagcdn.com/w320/za.png",
"Turkey":"https://flagcdn.com/w320/tr.png"
}

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

flag_url = flags[country]

# flag background (fixed)
st.markdown(f"""
<div style="
background-image: url('{flag_url}');
background-size: contain;
background-repeat: no-repeat;
background-position: center;
padding:80px;
border-radius:15px;
text-align:center;
font-size:26px;
font-weight:bold;
color:black;
background-color:white;
">

<h2>{country} - {year}</h2>

Customers Added: {added} <br><br>
Customers Cancelled: {cancelled}

</div>
""", unsafe_allow_html=True)

st.subheader("Customer Data")

st.dataframe(filtered)