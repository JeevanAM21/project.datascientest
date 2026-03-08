import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="California Housing Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ---------------------------------
# Title
# ---------------------------------
st.title("🏠 California Housing Analytics Dashboard")
st.markdown("Interactive Data Exploration of the California Housing Dataset")

# ---------------------------------
# Load Dataset
# ---------------------------------
@st.cache_data
def load_data():
    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["Target"] = data.target
    return df

df = load_data()

# ---------------------------------
# Sidebar Navigation
# ---------------------------------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Page",
    [
        "Dataset Overview",
        "Feature Distribution",
        "Correlation Analysis",
        "Pairplot Analysis",
        "Dataset Table"
    ]
)

# ---------------------------------
# Feature Meaning Table
# ---------------------------------
variable_meaning = {
    "MedInc": "Median income in block group",
    "HouseAge": "Median house age in block group",
    "AveRooms": "Average number of rooms per household",
    "AveBedrms": "Average number of bedrooms per household",
    "Population": "Population of block group",
    "AveOccup": "Average number of household members",
    "Latitude": "Latitude of block group",
    "Longitude": "Longitude of block group",
    "Target": "Median house value (in $100,000s)"
}

variable_df = pd.DataFrame(
    list(variable_meaning.items()),
    columns=["Feature", "Description"]
)

# ---------------------------------
# Dataset Overview
# ---------------------------------
if menu == "Dataset Overview":

    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.subheader("Feature Description")
    st.dataframe(variable_df)

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

# ---------------------------------
# Feature Distribution
# ---------------------------------
elif menu == "Feature Distribution":

    st.header("Feature Distribution")

    feature = st.selectbox(
        "Select Feature",
        df.columns
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Histogram")

        fig, ax = plt.subplots()
        sns.histplot(df[feature], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

    with col2:

        st.subheader("Boxplot")

        fig2, ax2 = plt.subplots()
        sns.boxplot(x=df[feature], ax=ax2)
        st.pyplot(fig2)

# ---------------------------------
# Correlation Analysis
# ---------------------------------
elif menu == "Correlation Analysis":

    st.header("Feature Correlation Heatmap")

    fig3, ax3 = plt.subplots(figsize=(10,6))

    sns.heatmap(
        df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax3
    )

    st.pyplot(fig3)

# ---------------------------------
# Pairplot Analysis
# ---------------------------------
elif menu == "Pairplot Analysis":

    st.header("Pairplot of Key Features")

    selected_features = st.multiselect(
        "Select Features",
        df.columns,
        default=["MedInc","HouseAge","AveRooms","Target"]
    )

    if len(selected_features) >= 2:

        pairplot = sns.pairplot(
            df[selected_features],
            diag_kind="kde"
        )

        st.pyplot(pairplot.fig)

# ---------------------------------
# Dataset Table
# ---------------------------------
elif menu == "Dataset Table":

    st.header("Dataset Viewer")

    rows = st.slider(
        "Select number of rows to display",
        5,
        100,
        10
    )

    st.dataframe(df.head(rows))

# ---------------------------------
# Insights Section
# ---------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("Key Insights")

st.sidebar.write("""
• Median income strongly affects house prices  
• Some features show skewed distributions  
• Outliers appear in AveRooms and AveOccup  
• Geographic features influence house value  
""")