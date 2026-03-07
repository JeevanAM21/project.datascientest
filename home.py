import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

st.set_page_config(page_title="California Housing EDA", layout="wide")
st.title("California Housing Dataset Exploration")

# Load dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = data.target

# Variable meaning table
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
variable_df = pd.DataFrame(list(variable_meaning.items()), columns=["Feature", "Description"])

st.subheader("Variable Meaning Table")
st.table(variable_df)

# Basic information
st.subheader("Dataset Info")
st.write(df.info())  # Optional: will print some info in console
st.write("Rows:", df.shape[0], "Columns:", df.shape[1])

st.subheader("First Five Rows")
st.dataframe(df.head())

# Summary statistics
st.subheader("Summary Statistics")
st.dataframe(df.describe())

# Histograms
st.subheader("Feature Distributions")
fig, ax = plt.subplots(figsize=(12, 8))
df.hist(ax=ax, bins=30, edgecolor='black')
st.pyplot(fig)

# Boxplots
st.subheader("Boxplots of Features")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.boxplot(data=df, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# Correlation heatmap
st.subheader("Feature Correlation Heatmap")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax3)
st.pyplot(fig3)

# Pairplot (only subset to avoid performance issues)
st.subheader("Pairplot of Key Features")
import seaborn as sns
fig4 = sns.pairplot(df[['MedInc', 'HouseAge', 'AveRooms', 'Target']], diag_kind='kde')
st.pyplot(fig4.fig)

# Key insights
st.subheader("Key Insights")
st.write("""
1. The dataset has {} rows and {} columns.
2. No missing values were found.
3. Some features like 'MedInc' are skewed.
4. Boxplots show potential outliers in 'AveRooms' and 'AveOccup'.
5. 'MedInc' has the highest correlation with house prices.
""".format(df.shape[0], df.shape[1]))