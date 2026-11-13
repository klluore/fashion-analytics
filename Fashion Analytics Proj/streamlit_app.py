import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import your separate files
from Components.styling import apply_styling
from Components.text import show_heading
from Components.buttons import show_filters
from Components.graphs import show_payment_graph

# Load datasets
Retail_sales = pd.read_csv("Fashion_Retail_Sales.csv")

# Apply styling
apply_styling()

# Display heading
show_heading()

# Display filters
selected_payment = show_filters(Retail_sales)

# Filter dataset
filtered_sales = Retail_sales[
    Retail_sales["Payment Method"].isin(selected_payment)
]

# Display graph
show_payment_graph(filtered_sales)