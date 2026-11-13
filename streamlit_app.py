import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Fashion Data Visualization")

st.write
(
    "Application to visualize fashion data using Streamlit. Explore various datasets, analyze trends, and gain insights into fashion industry."
)

# loading data in
Retail_sales = pd.read_csv(
    "Fashion_Retail_Sales.csv",
    usecols=[
        "Customer Reference ID",
        "Item Purchased",
        "Purchase Amount (USD)",
        "Date Purchase",
        "Review Rating",
        "Payment"
    ]
)

st.header("Fashion Retail Sales Analysis")

# First graph = Payment Methods
st.subheader("Payment Method Trends")

Purchase_type = Retail_sales["Payment"].value_counts()

fig1, ax1 = plt.subplots(figsize=(8, 5))

Purchase_type.plot(
    kind="bar",
    color="skyblue",
    ax=ax1
)

ax1.set_title("Number of Sales Based on Payment Method")
ax1.set_xlabel("Payment Method")
ax1.set_ylabel("Number of Sales")
ax1.tick_params(axis="x", rotation=0)

fig1.tight_layout()

st.pyplot(fig1)

plt.close(fig1)


# Second graph = Items Purchased
st.subheader("Popular Items Purchased")

Item_type = Retail_sales["Item Purchased"].value_counts().sort_values()

fig2, ax2 = plt.subplots(figsize=(10, 10))

Item_type.plot(
    kind="barh",
    color="purple",
    ax=ax2
)

ax2.set_title("Number of Purchases Based on Item Type")
ax2.set_xlabel("Number of Purchases")
ax2.set_ylabel("Item Purchased")

fig2.tight_layout()

st.pyplot(fig2)

plt.close(fig2)
