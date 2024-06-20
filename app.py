import streamlit as st
from components.periodic_buttons import PeriodicTable

st.set_page_config(layout="wide")

st.title("Cyclic Voltammetry")

if "materials" not in st.session_state:
    st.session_state["materials"] = ""

materials = st.session_state["materials"]


searchbar, searchbutton = st.columns([5, 1])


with searchbar:
    search_bar_value = st.text_input(
        label="Element Input",
        placeholder="Select Element",
        label_visibility="collapsed",
        value=materials,
    )


with searchbutton:
    if st.button("Search"):
        st.switch_page("pages/1_entry-table.py")


PeriodicTable()
