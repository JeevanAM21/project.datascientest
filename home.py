import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Titanic Data Dashboard",
    page_icon="🚢",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------
st.title("🚢 Titanic Survival Data Dashboard")
st.markdown("Interactive Data Exploration and Visualization")

# -----------------------------------
# Load Dataset
# -----------------------------------
@st.cache_data
def load_data():
    df = sns.load_dataset("titanic")
    return df

df = load_data()

# -----------------------------------
# Sidebar Navigation
# -----------------------------------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Page",
    [
        "Dataset Overview",
        "Survival Analysis",
        "Feature Distribution",
        "Correlation Analysis",
        "Dataset Viewer"
    ]
)

# -----------------------------------
# Feature Description Table
# -----------------------------------
feature_description = {
    "survived": "Survival (0 = No, 1 = Yes)",
    "pclass": "Passenger class",
    "sex": "Passenger gender",
    "age": "Passenger age",
    "sibsp": "Number of siblings/spouses aboard",
    "parch": "Number of parents/children aboard",
    "fare": "Passenger fare",
    "embarked": "Port of embarkation",
    "class": "Travel class",
    "who": "Passenger category (man, woman, child)",
    "adult_male": "Whether passenger is an adult male",
    "deck": "Deck of the ship",
    "embark_town": "Town where passenger embarked",
    "alive": "Survival status"
}

feature_df = pd.DataFrame(
    list(feature_description.items()),
    columns=["Feature", "Description"]
)

# -----------------------------------
# Dataset Overview
# -----------------------------------
if menu == "Dataset Overview":

    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Passengers", df.shape[0])
    col2.metric("Total Features", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.subheader("Feature Description")
    st.dataframe(feature_df)

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

# -----------------------------------
# Survival Analysis
# -----------------------------------
elif menu == "Survival Analysis":

    st.header("Survival Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Survival Count")

        fig, ax = plt.subplots()

        sns.countplot(
            x="survived",
            data=df,
            palette="Set2",
            ax=ax
        )

        ax.set_xticklabels(["Not Survived", "Survived"])

        st.pyplot(fig)

    with col2:

        st.subheader("Survival by Gender")

        fig2, ax2 = plt.subplots()

        sns.countplot(
            x="sex",
            hue="survived",
            data=df,
            palette="coolwarm",
            ax=ax2
        )

        st.pyplot(fig2)

# -----------------------------------
# Feature Distribution
# -----------------------------------
elif menu == "Feature Distribution":

    st.header("Feature Distribution")

    numeric_cols = df.select_dtypes(include=['float64','int64']).columns

    feature = st.selectbox(
        "Select Numerical Feature",
        numeric_cols
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Histogram")

        fig, ax = plt.subplots()

        sns.histplot(
            df[feature],
            kde=True,
            bins=30,
            color="skyblue",
            ax=ax
        )

        st.pyplot(fig)

    with col2:

        st.subheader("Boxplot")

        fig2, ax2 = plt.subplots()

        sns.boxplot(
            x=df[feature],
            color="orange",
            ax=ax2
        )

        st.pyplot(fig2)

# -----------------------------------
# Correlation Analysis
# -----------------------------------
elif menu == "Correlation Analysis":

    st.header("Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['float64','int64'])

    fig3, ax3 = plt.subplots(figsize=(10,6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax3
    )

    st.pyplot(fig3)

# -----------------------------------
# Dataset Viewer
# -----------------------------------
elif menu == "Dataset Viewer":

    st.header("Dataset Table")

    rows = st.slider(
        "Select number of rows",
        5,
        100,
        10
    )

    st.dataframe(df.head(rows))

# -----------------------------------
# Sidebar Insights
# -----------------------------------
st.sidebar.markdown("---")

st.sidebar.subheader("Key Insights")

st.sidebar.write("""
• Women had higher survival rates than men  
• First-class passengers survived more  
• Fare price influenced survival probability  
• Age distribution shows most passengers were young adults  
""")