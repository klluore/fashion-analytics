import streamlit as st

def show_filters(Retail_sales):

    st.sidebar.title("Explore the Data")

    payment_options = Retail_sales["Payment Method"].unique().tolist()

    selected_payment = st.sidebar.multiselect
    (
        "Select Payment Method",
        payment_options,
        default=payment_options
    )

    return selected_payment