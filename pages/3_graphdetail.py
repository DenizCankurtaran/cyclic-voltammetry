import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from util.normalize_entries import normalize_entries
from util.plot_graph import plot_graph

if "multiplot" not in st.session_state:
    st.session_state["multiplot"] = []

entries = st.session_state["multiplot"]

st.set_page_config(layout="wide")
st.title("Chart")
col1, col2 = st.columns([3, 2])

with col1:
    plot_graph(entries, "Detail Entries")

with col2:
    data = {
        "Property": ["Placeholder 1", "Placeholder 2", "Placeholder 3"],
        "Value": ["aa", "aa", "Ag"],
    }
    st.table(data)