import streamlit as st
import plotly.graph_objs as go
from normalization.normalization import (
    normalize_ref,
    normalize_electrolyte_concentration,
    normalize_scan_rate,
)

if "multiplot" not in st.session_state:
    st.session_state["multiplot"] = []

entries = st.session_state["multiplot"]
# entries = [copy.copy(entry) for entry in original_entries]

st.title("Example Chart")

def normalize_entries(entries, ref_electrode=None, c_ref=None, ref_scan_rate=None):
    normalized_entries = []
    for entry in entries:
        copied_df = entry.df.copy()
        if ref_electrode:
            delta_ref = normalize_ref(entry, ref_electrode)
            copied_df["E"] = copied_df["E"] + delta_ref
        if c_ref is not None:
            try:
                delta_ref = normalize_electrolyte_concentration(entry, c_ref)
                copied_df["E"] = copied_df["E"] + delta_ref
            except:
                print("No electrolyte entry found")
                continue
        if ref_scan_rate is not None:
            delta_ref = normalize_scan_rate(entry, ref_scan_rate)
            copied_df["j"] = copied_df["j"] * delta_ref
        normalized_entries.append({"df": copied_df, "identifier": entry.identifier})
    return normalized_entries

def plot_graph(entries, title):
    fig = go.Figure()
    for entry in entries:
        # print(entries)
        fig.add_trace(
            go.Scatter(x=entry["df"]["E"], y=entry["df"]["j"], name=entry["identifier"], mode="lines")
        )
    fig.update_layout(title=title)
    st.plotly_chart(fig)

# print(st.session_state['multiplot'])

normalize_checkbox = st.checkbox("Normalize", True)
normalize_electrolyte_checkbox = st.checkbox("Normalize Electrolyte Concentration")
normalize_scan_rate_checkbox = st.checkbox("Normalize Scan Rate")

ref_electrode = None
c_ref = None
ref_scan_rate = None

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
    ], index=0)

if normalize_electrolyte_checkbox:
    c_ref = 1.0

if normalize_scan_rate_checkbox:
    ref_scan_rate = 1.0 

normalized_entries = normalize_entries(entries, ref_electrode, c_ref, ref_scan_rate)

col1, col2 = st.columns([3, 2])
with col1:
    plot_graph(normalized_entries, "Normalized Entries")

with col2:
    data = {
        "Property": ["Placeholder 1", "Placeholder 2", "Placeholder 3"],
        "Value": [47, 107.8682, "Ag"]
    }
    st.table(data)
