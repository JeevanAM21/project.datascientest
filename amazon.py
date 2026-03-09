import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Amazon Prime Dashboard", layout="wide")

# Amazon background
amazon_bg = "https://wallpapers.com/images/hd/amazon-prime-video-logo-portal-5ioemdo56totmacf.jpg"

# FULL PAGE BACKGROUND
st.markdown(f"""
<style>
.stApp {{
background-image: url("{amazon_bg}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}}
</style>
""", unsafe_allow_html=True)

# Session state
if "page" not in st.session_state:
    st.session_state.page = "login"

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

names = [
"Rahul Sharma","Amit Patel","Priya Singh","John Smith","Emma Brown",
"Akira Tanaka","Carlos Diaz","Maria Lopez","David Miller","Sarah Wilson",
"Daniel Lee","Sophia Garcia","James Anderson","Olivia Martin",
"Lucas Rossi","Liam Johnson","Noah Kim","Mia Chen","Arjun Reddy","Fatima Ali"
]

years = list(range(2015,2026))

# Create dataset
data=[]
cid=1000

for year in years:
    for i in range(200):
        cid+=1
        data.append([
            f"C{cid}",
            random.choice(names),
            random.choice(countries),
            year,
            random.choice(["Added","Cancelled"])
        ])

df=pd.DataFrame(data,columns=["Customer_ID","Customer_Name","Country","Year","Status"])

# LOGIN PAGE
if st.session_state.page=="login":

    st.title("Amazon Prime Login")

    username=st.text_input("Username")
    password=st.text_input("Password",type="password")

    if st.button("Login"):
        st.session_state.page="dashboard"
        st.session_state.country="India"
        st.session_state.year=2025
        st.rerun()

# DASHBOARD
elif st.session_state.page=="dashboard":

    st.title("Amazon Prime Customer Dashboard")

    col1,col2=st.columns(2)

    country=col1.selectbox("Select Country",countries,index=countries.index(st.session_state.country))
    year=col2.selectbox("Select Year",years,index=years.index(st.session_state.year))

    st.session_state.country=country
    st.session_state.year=year

    filtered=df[(df["Country"]==country)&(df["Year"]==year)]

    added=filtered[filtered["Status"]=="Added"].shape[0]
    cancelled=filtered[filtered["Status"]=="Cancelled"].shape[0]

    flag=flags[country]

    st.image(flag,width=80)

    st.header(f"{country} - {year}")

    col1,col2=st.columns(2)
    col1.metric("Customers Added",added)
    col2.metric("Customers Cancelled",cancelled)

    chart=pd.DataFrame({
        "Status":["Added","Cancelled"],
        "Customers":[added,cancelled]
    })

    st.subheader("Customer Analysis")
    st.bar_chart(chart.set_index("Status"))

    st.subheader("Customer Data")
    st.dataframe(filtered)

    if st.button("Logout"):
        st.session_state.page="login"
        st.rerun()