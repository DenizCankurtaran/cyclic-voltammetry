import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from util.normalize_entries import normalize_entries
from util.plot_graph import plot_graph
from components.nav_bar import NavBar
from db.entries import get_all_entries

# Necessary to format the subitems in the tables.
# This will move subitems to the right for a better overview.
def format_item(content):
    return f"""
    <ul style="list-style-type:none;">
        <li style="text-indent: -1em; padding-left: 1em;">- {content}</li>
    </ul>
    """

# Retrive all entries and search for the entry used
# in the query parameter, so only that one is displayed
if "name" not in st.query_params:
    st.query_params["name"] = []

name = st.query_params["name"]
all_entries = get_all_entries()
entry = all_entries[name]

# The normalize_entries function is only called to display
# the graph properly, the detail graph itself shows the values
# non-normalized.
entries = normalize_entries(
    [entry], ref_electrode=None, c_ref=None, ion=None, ref_scan_rate=None
)

st.set_page_config(layout="wide")
NavBar("Detail")

# Scrollable table, instead of scrolling the entire
# page down depending on how many table entries exist.
css=f'''
div.stTabs {{
    height: 600px;
    overflow-y: scroll;
    overflow-x: hidden;
}}
'''
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title(f"Detail view for {name}")
# Columns used to have the graph and table next to eachother,
# instead of having the table and graph displayed vertically.
col1, col2 = st.columns([3, 2])

# Get the matching X and Y Label of an entry and set those as the label,
# alongside of plotting the graph while having "Detail Entries" as the header.
with col1:
    labels = entries[0]
    columns = labels["df"].columns
    x_label = columns[1]
    y_label = columns[2]
    plot_graph(entries, "Detail Entries", x_label, y_label)

with col2:
    #Define the Tabs that should be used within the page
    tab1, tab2, tab3 = st.tabs(
        ["ELECTROCHEMICAL SYSTEM", "ENTRY SOURCE", "BIBLIOGRAPHY"]
    )
    # - Electrochemical System Tab
    with tab1:
        st.header("ELECTROCHEMICAL SYSTEM")
        electrochemical_system = entry.system

        # Gather all Electrochemical System properties and check,
        # if a matching attribute is found. Only display it if
        # that's the case. The following ones display all electrodes.
        for electrode in electrochemical_system["electrodes"]:
            st.subheader(f"{electrode['function'].capitalize()} ({electrode['name']}):")
            if hasattr(electrode, "material"):
                st.text(f"Material: {electrode['material']}")
            if hasattr(electrode, "type"):
                st.text(f"Type: {electrode['type']}")
            if hasattr(electrode, "shape"):
                st.text(f"Shape: {electrode['shape']['type']}")
            if hasattr(electrode, "crystallographic orientation"):
                st.text(
                    f"Crystallographic orientation: {electrode['crystallographic orientation']}"
                )
            if hasattr(electrode, "preparation procedure"):
                st.text(
                    f"Preparation procedure: {','.join(electrode['preparation procedure']['description'])}"
                )

        # Display all electrolytes and it's components, checking if
        # it has matching attributes to display.
        st.subheader("Electrolyte:")
        electrolyte = electrochemical_system["electrolyte"]
        st.text(f"Components:")
        for component in electrolyte['components']:
            st.text('Concentration:')
            if hasattr(component, 'name'):
                st.markdown(format_item(f"Name: {component['name']}"), unsafe_allow_html=True)
            if hasattr(component, 'type'):
                st.markdown(format_item(f"Type: {component['type']}"), unsafe_allow_html=True)
            if hasattr(component, 'concentration'):
                if hasattr(component, 'unit'):
                    st.markdown(format_item(f"Unit: {component['concentration']['unit']}"), unsafe_allow_html=True)
                if hasattr(component, 'value'):
                    st.markdown(format_item(f"Value: {component['concentration']['value']}"), unsafe_allow_html=True)

               
        # Display the temperature and the unit of a electrolyte
        try:
            temp_unit=electrochemical_system["electrolyte"]["temperature"]["unit"]
            temp_value=electrochemical_system["electrolyte"]["temperature"]["value"]
            if temp_unit or temp_value:
                st.text(f"Temperature:")
            if temp_unit:
                st.markdown(format_item(f"Unit: {temp_unit}"), unsafe_allow_html=True)

            if temp_value:
                st.markdown(format_item(f"Value: {temp_value}"), unsafe_allow_html=True)
        except:
            print("No temperature found")

        # Display the Scan rate of a electrolyte
        try:
            scan_rate = entry.figure_description['scan rate']
            st.subheader("Scan rate")
            if hasattr(scan_rate, 'unit'):
                st.text(f"Unit: {scan_rate['unit']}")       
            if hasattr(scan_rate, 'value'):
                st.text(f"Value: {scan_rate['value']}")
        except: 
            print("No scan rate")

    # - Entry Source Tab
    # Similarily to the first tab, check if there are
    # matching attributes inside the entry source,
    # and display matching attributes
    with tab2:
        st.header("ENTRY SOURCE")
        entry_source = entry.source
        if hasattr(entry_source, 'citation_key'):
            st.text(f"Citation key: {entry_source.citation_key}")
        if hasattr(entry_source, 'url'):
            st.text(f"URL: {entry_source.url}")
        if hasattr(entry_source, 'techniques'):
            st.text(f"Techniques: {','.join(entry_source.techniques)}")
        if hasattr(entry_source, 'figure'):
            st.text(f"Figure: {entry_source.figure}")
        if hasattr(entry_source, 'curve'):
            st.text(f"Curve: {entry_source.curve}")

    # - Bibliography Tab
    # Loop through all fields first inside the Bibliography
    # of the entry and display those. After that, loop
    # through all involved persons and display those as well
    with tab3:
        st.header("BIBLIOGRAPHY")
        bibliography = entry.bibliography
        st.text(f"Type: {bibliography.type}")

        fields_dict = dict(bibliography.fields)
        for field, value in fields_dict.items():
            st.text(f"{field.capitalize()}: {value}")

        persons = bibliography.persons.get("author")
        person_names = [f"{person}" for person in persons]
        st.text("Authors: " + "; ".join(person_names))
