import streamlit as st
import copy
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

def normalize_entries(entries, ref_electrode):
    normalized_entries = []
    for entry in entries:
        delta_ref = normalize_ref(entry, ref_electrode)
        copied_df = entry.df.copy()
        copied_df["E"] = copied_df["E"] + delta_ref
        normalized_entries.append({"df": copied_df, "identifier": entry.identifier})
    return normalized_entries


def normalize_entries_electrolyte(entries):
    c_ref = 1.0
    normalized_entries = []
    for entry in entries:
        try:
            delta_ref = normalize_electrolyte_concentration(entry, c_ref)
            copied_df = entry.df.copy()
            copied_df["E"] = copied_df["E"] + delta_ref
            normalized_entries.append({"df": copied_df, "identifier": entry.identifier})
        except:
            print("No electrolyte entry found")
            continue
    return normalized_entries

def normalize_entries_scan_rate(entries):
    ref_scan_rate = 1.0
    normalized_entries = []
    for entry in entries:
        delta_ref = normalize_scan_rate(entry, ref_scan_rate)
        copied_df = entry.df.copy()
        copied_df["j"] = copied_df["j"] * delta_ref
        normalized_entries.append({"df": copied_df, "identifier": entry.identifier})
    return normalized_entries


def plot_graph(entries, title):
    fig = go.Figure()
    for entry in entries:
        print(entries)
        fig.add_trace(
            go.Scatter(x=entry["df"]["E"], y=entry["df"]["j"], name=entry["identifier"], mode="lines")
        )
    fig.update_layout(title=title)
    st.plotly_chart(fig)

# print(st.session_state['multiplot'])

normalize_checkbox = st.checkbox("Normalize", True)
normalize_electrolyte_checkbox = st.checkbox("Normalize Electrolyte Concentration")
normalize_scan_rate_checkbox = st.checkbox("Normalize Scan Rate")

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
    entries = normalize_entries(entries, ref_electrode)
    plot_graph(entries, "Normalized Entries")

if normalize_electrolyte_checkbox:
    entries = normalize_entries_electrolyte(entries)
    plot_graph(entries, "Electrolyte Concentration")

if normalize_scan_rate_checkbox:
    entries = normalize_entries_scan_rate(entries)
    plot_graph(entries, "Scan rate")
