import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import io

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("Machine Learning model to predict customer churn")

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to",
    ["Upload Data", "EDA Analysis", "Train Model", "Customer Lookup"]
)

# -----------------------------
# Upload Dataset
# -----------------------------
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    # -----------------------------
    # KPI Metrics
    # -----------------------------
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", data.shape[0])
    col2.metric("Columns", data.shape[1])
    col3.metric("Missing Values", data.isnull().sum().sum())

    # -----------------------------
    # Upload Data Page
    # -----------------------------
    if menu == "Upload Data":

        st.subheader("Dataset Preview")
        st.dataframe(data.head())

        st.subheader("Dataset Info")

        buffer = io.StringIO()
        data.info(buf=buffer)
        st.text(buffer.getvalue())

        st.subheader("Statistical Summary")
        st.dataframe(data.describe())

    # -----------------------------
    # EDA Analysis
    # -----------------------------
    elif menu == "EDA Analysis":

        st.subheader("Exploratory Data Analysis")

        col1, col2 = st.columns(2)

        with col1:
            if 'Churn' in data.columns:
                st.write("### Churn Distribution")
                fig, ax = plt.subplots()
                sns.countplot(x='Churn', data=data, ax=ax)
                st.pyplot(fig)
            else:
                st.warning("No 'Churn' column found")

        with col2:
            st.write("### Correlation Heatmap")

            fig, ax = plt.subplots(figsize=(6,4))
            sns.heatmap(data.corr(numeric_only=True), cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    # -----------------------------
    # Model Training
    # -----------------------------
    elif menu == "Train Model":

        st.subheader("Train Machine Learning Model")

        if 'Churn' not in data.columns:
            st.error("Dataset must contain 'Churn' column")

        else:

            X = pd.get_dummies(data.drop('Churn', axis=1), drop_first=True)
            y = data['Churn'].apply(lambda x: 1 if str(x).lower()=="yes" else 0)

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=42
            )

            model = LogisticRegression(max_iter=1000)

            if st.button("Train Model"):

                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)

                acc = accuracy_score(y_test, y_pred)

                st.success(f"Model Accuracy: {acc:.2f}")

                st.subheader("Classification Report")
                st.text(classification_report(y_test, y_pred))

                st.subheader("Confusion Matrix")

                fig, ax = plt.subplots()
                sns.heatmap(
                    confusion_matrix(y_test, y_pred),
                    annot=True,
                    fmt='d',
                    cmap="Blues",
                    ax=ax
                )
                st.pyplot(fig)

    # -----------------------------
    # Customer Lookup (Row Number Only)
    # -----------------------------
    elif menu == "Customer Lookup":

        st.subheader("Customer Search by Row Number")

        max_row = len(data)

        row_number = st.number_input(
            f"Enter row number (1 - {max_row})",
            min_value=1,
            max_value=max_row,
            step=1
        )

        if row_number:

            row_index = row_number - 1
            customer_row = data.iloc[row_index]

            st.success(f"Customer Data for Row {row_number}")
            st.json(customer_row.to_dict())

else:
    st.info("Upload dataset from sidebar to start.")