import streamlit as st
import pandas as pd

st.title("Customer Product Lookup App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # -----------------------------
    # Customer lookup
    # -----------------------------
    st.subheader("Check Products Purchased by Customer ID")
    
    if 'customerID' not in data.columns:
        st.error("No column named 'customerID' found in the dataset.")
    else:
        customer_id = st.text_input("Enter Customer ID:")
        
        if customer_id:
            # Filter the customer
            customer_data = data[data['customerID'] == customer_id]
            
            if customer_data.empty:
                st.warning("Customer ID not found!")
            else:
                # Assuming 'TotalProducts' is the column showing how many products they purchased
                if 'TotalProducts' in customer_data.columns:
                    total_products = customer_data['TotalProducts'].values[0]
                    st.success(f"Customer {customer_id} purchased {total_products} products.")
                else:
                    st.warning("No column named 'TotalProducts' found in the dataset.")
else:
    st.info("Please upload a CSV file to continue.")