import streamlit as st
from components.periodic_table import PeriodicTable
from db.entries import get_all_entries

st.set_page_config(layout="wide")

st.title("Cyclic Voltammetry")

if "materials" not in st.session_state:
    st.session_state["materials"] = ""

if "all_entries" not in st.session_state:
    st.session_state["all_entries"] = []

if "system" not in st.session_state:
    st.session_state["system"] = "aqueous"

materials = st.session_state["materials"]


search_bar, select_system, search_button = st.columns([4, 1, 1])

all_entries = get_all_entries()
st.session_state["all_entries"] = all_entries


with search_bar:
    search_bar_value = st.text_input(
        label="Element Input",
        placeholder="Select Element",
        label_visibility="collapsed",
        value=materials,
    )
    st.session_state["materials"] = search_bar_value

with select_system:
    select_system_value = st.selectbox(
        "System",
        [
            "Aqueous",
            "Non aqueous",
        ],
        index=0,
        label_visibility="collapsed"
    )
    if select_system_value == "Aqueous":
        st.session_state["system"] = "aqueous"
    else:
        st.session_state["system"] = "ionic liquid"


with search_button:
    if st.button("Search"):
        st.switch_page("pages/1_entry-table.py")


PeriodicTable(all_entries.materials())
