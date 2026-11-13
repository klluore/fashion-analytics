import streamlit as st
import matplotlib.pyplot as plt

# payment methods graph
def show_payment_graph(filtered_sales):

    st.subheader("Payment Method Trends")

    Purchase_type = filtered_sales["Payment Method"].value_counts()

    fig, ax = plt.subplots()

    Purchase_type.plot(kind="bar", ax=ax)

    ax.set_title("Number of Sales by Payment Method")
    ax.set_xlabel("Payment Method")
    ax.set_ylabel("Number of Sales")

    st.pyplot(fig)
    plt.close(fig)

# item purchased graph
def show_clothing_graph(filtered_sales):

    st.subheader("Popular Clothing Items")

    Item_type = filtered_sales["Item Purchased"].value_counts().sort_values()

    fig, ax = plt.subplots(figsize=(10, 8))

    Item_type.plot(kind="barh", color="purple", ax=ax)

    ax.set_title("Number of Purchases Based on Item Type")
    ax.set_xlabel("Number of Purchases")
    ax.set_ylabel("Item Purchased")

    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)