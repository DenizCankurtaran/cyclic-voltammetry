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

ref_electrode = None
c_ref = None
ion = None
ref_scan_rate = None

col1, col2 = st.columns([2, 1])

with col1:
    normalize_checkbox = st.checkbox("Normalize", True)
    normalize_electrolyte_checkbox = st.checkbox("Normalize Electrolyte Concentration")
    normalize_scan_rate_checkbox = st.checkbox("Normalize Scan Rate")

with col2:
    if normalize_checkbox:
        ref_electrode = st.selectbox('Select Reference Electrode', [
            'Ag/AgCl', 
            'Ag/AgCl-sat', 
            'Ag/AgCl_3M', 
            'Hg/HgO/0.1 M NaOH', 
            'RHE', 
            'SCE', 
            'wire', 
            'SHE', 
            'NCE'
        ], index=7)

    if normalize_electrolyte_checkbox:
        ion = st.selectbox('Select Reference Electrolyte', [
            'Br',
        ], index=0)
        c_ref = 1.0

    if normalize_scan_rate_checkbox:
        ref_scan_rate = st.selectbox('Select Reference Scanrate', [
            1.0, 
            2.0,
            3.0,
            4.0,
        ], index=0)

normalized_entries = normalize_entries(entries, ref_electrode, c_ref, ion, ref_scan_rate)

col3, col4 = st.columns([3, 2])

with col1:
    plot_graph(normalized_entries, "Normalized Entries")

with col2:
    identifiers = [entry["identifier"] for entry in normalized_entries]
    for entry in normalized_entries:
        entry["url"] = "/graphdetail"
    df = pd.DataFrame({
        "Elements": identifiers,
        "url": [entry["url"] for entry in normalized_entries]
    })
    st.data_editor(
        df,
        column_config={
            "url": st.column_config.LinkColumn("Elements", display_text="Detail View"),
        },
        hide_index=True
    )
