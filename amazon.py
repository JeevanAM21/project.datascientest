import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Amazon Prime Dashboard", layout="wide")

# Amazon background
amazon_bg = "https://wallpapers.com/images/hd/amazon-prime-video-logo-portal-5ioemdo56totmacf.jpg"

# Countries
countries = [
"India","United States","United Kingdom","Canada","Australia",
"Germany","France","Japan","South Korea","Brazil",
"Mexico","Italy","Spain","Netherlands","Sweden",
"Norway","Denmark","Switzerland","Singapore","Malaysia",
"Thailand","Indonesia","UAE","South Africa","Turkey"
]

# Flags
flags = {
"India":"https://flagcdn.com/w80/in.png",
"United States":"https://flagcdn.com/w80/us.png",
"United Kingdom":"https://flagcdn.com/w80/gb.png",
"Canada":"https://flagcdn.com/w80/ca.png",
"Australia":"https://flagcdn.com/w80/au.png",
"Germany":"https://flagcdn.com/w80/de.png",
"France":"https://flagcdn.com/w80/fr.png",
"Japan":"https://flagcdn.com/w80/jp.png",
"South Korea":"https://flagcdn.com/w80/kr.png",
"Brazil":"https://flagcdn.com/w80/br.png",
"Mexico":"https://flagcdn.com/w80/mx.png",
"Italy":"https://flagcdn.com/w80/it.png",
"Spain":"https://flagcdn.com/w80/es.png",
"Netherlands":"https://flagcdn.com/w80/nl.png",
"Sweden":"https://flagcdn.com/w80/se.png",
"Norway":"https://flagcdn.com/w80/no.png",
"Denmark":"https://flagcdn.com/w80/dk.png",
"Switzerland":"https://flagcdn.com/w80/ch.png",
"Singapore":"https://flagcdn.com/w80/sg.png",
"Malaysia":"https://flagcdn.com/w80/my.png",
"Thailand":"https://flagcdn.com/w80/th.png",
"Indonesia":"https://flagcdn.com/w80/id.png",
"UAE":"https://flagcdn.com/w80/ae.png",
"South Africa":"https://flagcdn.com/w80/za.png",
"Turkey":"https://flagcdn.com/w80/tr.png"
}

# Names
names = [
"Rahul Sharma","Amit Patel","Priya Singh","John Smith","Emma Brown",
"Akira Tanaka","Carlos Diaz","Maria Lopez","David Miller","Sarah Wilson",
"Daniel Lee","Sophia Garcia","James Anderson","Olivia Martin",
"Lucas Rossi","Liam Johnson","Noah Kim","Mia Chen","Arjun Reddy","Fatima Ali"
]

# Generate data
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

st.title("Amazon Prime Customer Analytics")

# Type country
country_input = st.text_input("Type Country Name")

if country_input:

    filtered = df[df["Country"].str.lower() == country_input.lower()]

    if not filtered.empty:

        added = filtered[filtered["Status"]=="Added"].shape[0]
        cancelled = filtered[filtered["Status"]=="Cancelled"].shape[0]

        flag = flags.get(country_input,"")

        st.markdown(f"""
        <div style="
        background-image:url('{amazon_bg}');
        background-size:cover;
        padding:60px;
        border-radius:15px;
        text-align:center;
        color:white;
        font-size:26px;
        font-weight:bold;
        ">

        <img src="{flag}" width="80">

        <h2>{country_input}</h2>

        Customers Added: {added} <br><br>
        Customers Cancelled: {cancelled}

        </div>
        """, unsafe_allow_html=True)

        st.subheader("Customer Data")
        st.dataframe(filtered)

    else:
        st.warning("Country not found in dataset")