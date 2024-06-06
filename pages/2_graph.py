import streamlit as st
import plotly.graph_objs as go
from db.entries import get_entries, filter_Ag100Br
from normalization.normalization import normalize_ref, normalize_electrolyte_concentration, normalize_scan_rate

entries = get_entries(filter_Ag100Br)
st.title('Example Chart')

def normalize_entries(entries):
    for entry in entries:
        delta_ref = normalize_ref(entry, 'Ag/AgCl')
        entry.df["E"] = entry.df["E"] + delta_ref
    return entries

def normalize_entries_electrolyte(entries):
    c_ref = 1.0
    for entry in entries:
        delta_ref = normalize_electrolyte_concentration(entry, c_ref)
        entry.df["E"] = entry.df["E"] + delta_ref
    return entries

def normalize_entries_scan_rate(entries):
    ref_scan_rate = 1.0
    for entry in entries:
        delta_ref = normalize_scan_rate(entry, ref_scan_rate)
        entry.df["j"] = entry.df["j"] * delta_ref
    return entries

def plot_graph(entries, title):
    fig = go.Figure()
    for CV in entries:
        fig.add_trace(go.Scatter(
            x=CV.df["E"], 
            y=CV.df["j"], 
            name=CV.identifier, 
            mode="lines"
        ))
    fig.update_layout(title=title)
    st.plotly_chart(fig)

normalize_checkbox = st.checkbox('Normalize')
normalize_electrolyte_checkbox = st.checkbox('Normalize Electrolyte Concentration')
normalize_scan_rate_checkbox = st.checkbox('Normalize Scan Rate')

if normalize_checkbox:
    entries = normalize_entries(entries)
    plot_graph(entries, 'Normalized Entries')

if normalize_electrolyte_checkbox:
    entries = normalize_entries_electrolyte(entries)
    plot_graph(entries, 'Electrolyte Concentration')

if normalize_scan_rate_checkbox:
    entries = normalize_entries_scan_rate(entries)
    plot_graph(entries, 'Scan rate')
