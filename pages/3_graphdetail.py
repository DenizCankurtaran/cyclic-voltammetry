import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from util.normalize_entries import normalize_entries
from util.plot_graph import plot_graph
from db.entries import get_entry_by_name

if "name" not in st.query_params:
    st.query_params["name"] = []

name = st.query_params["name"]

get_entries = get_entry_by_name(name)
entries = normalize_entries(get_entries, ref_electrode="SHE", c_ref=None, ion=None, ref_scan_rate=None)

st.set_page_config(layout="wide")
st.title(f"Detail view for {name}")
col1, col2 = st.columns([3, 2])

with col1:
    plot_graph(entries, "Detail Entries")

with col2:
    data = {
        "Property": ["Placeholder 1", "Placeholder 2", "Placeholder 3"],
        "Value": ["aa", "aa", "Ag"],
    }
    st.table(data)