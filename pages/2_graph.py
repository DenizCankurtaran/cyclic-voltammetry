import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from util.normalize_entries import normalize_entries
from util.plot_graph import plot_graph
from util.get_thumbnail import get_thumbnail
from components.nav_bar import NavBar

# Retrive the selected items from the table,
# and use those to plot the graph depending on
# what was selected.
if "multiplot" not in st.session_state:
    st.session_state["multiplot"] = []

entries = st.session_state["multiplot"]

st.set_page_config(layout="wide")
NavBar("Graph")

st.title("Chart")

# Attributes for the normalization. They're set as None at first,
# and are later set depending on what normalization method is used.
ref_electrode = None
c_ref = None
ion = None
ref_scan_rate = None

# Used to format, so the checkboxes and dropdowns
# are next to eachother instead of being stacked
# on top of eachother.
col1, col2 = st.columns([2, 1])

with col1:
    normalize_checkbox = st.checkbox("Normalize Reference Electrode")

# List all available reference electrodes(see normalization/normalization.py)
# and set the reference electrode depending on what item is selected in the dropdown.
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

# Resetting the columns is necessary, otherwise it's not
# alligned with the dropdown field.
col1, col2 = st.columns([2, 1])

with col1:
    normalize_electrolyte_checkbox = st.checkbox("Normalize Electrolyte Concentration")

# List all available reference electrolytes and
# set the ion depending on what was selected
# (For now only BR is available)
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


# Resetting the columns is necessary, otherwise it's not
# alligned with the dropdown field.
col1, col2 = st.columns([2, 1])

with col1:
    normalize_scan_rate_checkbox = st.checkbox("Normalize Scan Rate")

# Allow the user to set a custom input for the scan rate.
# Defaults to 50
with col2:
    if normalize_scan_rate_checkbox:
        ref_scan_rate = st.number_input(
            "Select Reference Scanrate",
            min_value=0.0,
            value=50.0,
            step=0.5,
            format="%.1f",
        )

# Retrive the selected normilzation method / input, and save
# those to a variable, which will then be used to plot the graph.
normalized_entries = normalize_entries(
    entries, ref_electrode, c_ref, ion, ref_scan_rate
)

# Get the matching X and Y Label of an entry and set those as the label.
labels = normalized_entries[0]
columns = labels["df"].columns
x_label = columns[1]
y_label = columns[2]

plot_graph(normalized_entries, "Normalized Entries", x_label, y_label)

identifiers = []
graphs = []
urls = []

# Loop through all availabble entries inside the graph page,
# and create a small Table overview, displaying the name,
# a thumbnail and a Link to their respective Detail Page,
# which allows the user to look at the details of a certian element.
for index, entry in enumerate(normalized_entries):
    identifier = entry["identifier"]
    identifiers.append(identifier)

    graphs.append(
        get_thumbnail(entries[index], entries[index].package.resource_names[0])
    )

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
