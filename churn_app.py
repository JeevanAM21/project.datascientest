import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")
st.title("Customer Churn Prediction App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV
    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # Show dataset info
    st.subheader("Dataset Info")
    buffer = []
    data.info(buf=buffer)
    st.text(buffer)

    # Show dataset description
    st.subheader("Dataset Description")
    st.write(data.describe())

    # Basic visualization example
    st.subheader("Churn Count Plot")
    if 'Churn' in data.columns:
        plt.figure(figsize=(6,4))
        sns.countplot(x='Churn', data=data)
        st.pyplot(plt)
    else:
        st.warning("No column named 'Churn' found for plotting.")

    # Simple model training (optional)
    if st.checkbox("Train Model"):
        if 'Churn' not in data.columns:
            st.error("Cannot train model: 'Churn' column is missing.")
        else:
            # Convert categorical columns to dummy variables
            X = pd.get_dummies(data.drop('Churn', axis=1), drop_first=True)
            y = data['Churn'].apply(lambda x: 1 if x=='Yes' else 0)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            st.subheader("Model Performance")
            st.write("Accuracy:", accuracy_score(y_test, y_pred))
            st.write("Classification Report:")
            st.text(classification_report(y_test, y_pred))
            st.write("Confusion Matrix:")
            fig, ax = plt.subplots()
            sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', ax=ax)
            st.pyplot(fig)
else:
    st.info("Please upload a CSV file to continue.")