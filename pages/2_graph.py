import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from util.normalize_entries import normalize_entries
from util.plot_graph import plot_graph
from util.get_thumbnail import get_thumbnail

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

with col2:
    if normalize_checkbox:
        ref_electrode = st.selectbox(
            "Select Reference Electrode",
            [
                "Ag/AgCl",
                "Ag/AgCl-sat",
                "Ag/AgCl_3M",
                "Hg/HgO/0.1 M NaOH",
                "RHE",
                "SCE",
                "wire",
                "SHE",
                "NCE",
            ],
            index=7,
        )
col1, col2 = st.columns([2, 1])

with col1:
    normalize_electrolyte_checkbox = st.checkbox("Normalize Electrolyte Concentration")


with col2:
    if normalize_electrolyte_checkbox:
        ion = st.selectbox(
            "Select Reference Electrolyte (Experimental)",
            [
                "Br",
            ],
            index=0,
        )
        c_ref = 1.0


col1, col2 = st.columns([2, 1])

with col1:
    normalize_scan_rate_checkbox = st.checkbox("Normalize Scan Rate")

with col2:
    if normalize_scan_rate_checkbox:
        ref_scan_rate = st.number_input(
            "Select Reference Scanrate",
            min_value=0.0,
            value=5.0,
            step=0.1,
        )

normalized_entries = normalize_entries(
    entries, ref_electrode, c_ref, ion, ref_scan_rate
)

labels = normalized_entries[0]
columns = labels["df"].columns
x_label = columns[1]
y_label = columns[2]

plot_graph(normalized_entries, "Normalized Entries", x_label, y_label)

identifiers = []
graphs = []
urls = []

for index, entry in enumerate(normalized_entries):
    identifier = entry["identifier"]
    identifiers.append(identifier)

    graphs.append(get_thumbnail(entries[index]))

    urls.append(f"/detail?name={identifier}")

df = pd.DataFrame({"Name": identifiers, "Graph": graphs, "url": urls})

st.dataframe(
    df,
    column_config={
        "Graph": st.column_config.ImageColumn("Graph"),
        "url": st.column_config.LinkColumn("Elements", display_text="Detail View"),
    },
    hide_index=True,
)
