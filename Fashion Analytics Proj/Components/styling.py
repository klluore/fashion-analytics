import streamlit as st

def apply_styling():
    st.markdown("""
        <style>
        .stApp {
            background-color: #F2F0EF;
        }

        h1 {
            color: #3d81ff;
        }

        </style>
    """, unsafe_allow_html=True)