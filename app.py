import streamlit as st
from components.periodic_buttons import PeriodicTable

st.set_page_config(layout="wide")

st.title('Cyclic Voltammetry')

searchbar, searchbutton = st.columns([5, 1])

with searchbar:
    st.text_input(label="Element Input", placeholder="Select Element", label_visibility='collapsed')
with searchbutton:
    st.button("Search")


PeriodicTable()