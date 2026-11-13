import streamlit as st
import matplotlib.pyplot as plt

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