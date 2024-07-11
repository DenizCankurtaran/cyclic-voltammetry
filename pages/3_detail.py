import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from util.normalize_entries import normalize_entries
from util.plot_graph import plot_graph
from components.nav_bar import NavBar
from db.entries import get_all_entries

if "name" not in st.query_params:
    st.query_params["name"] = []

name = st.query_params["name"]

all_entries = get_all_entries()
entry = all_entries[name]

entries = normalize_entries(
    [entry], ref_electrode="SHE", c_ref=None, ion=None, ref_scan_rate=None
)

st.set_page_config(layout="wide")
NavBar("Detail")

st.title(f"Detail view for {name}")
col1, col2 = st.columns([3, 2])

with col1:
    labels = entries[0]
    columns = labels["df"].columns
    x_label = columns[1]
    y_label = columns[2]
    plot_graph(entries, "Detail Entries", x_label, y_label)

with col2:
    tab1, tab2, tab3 = st.tabs(
        ["ELECTROCHEMICAL SYSTEM", "ENTRY SOURCE", "BIBLIOGRAPHY"]
    )
    with tab1:
        st.header("ELECTROCHEMICAL SYSTEM")
        electrochemical_system = entry.system

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

        st.subheader("Electrolyte:")
        electrolyte = electrochemical_system["electrolyte"]

        st.text(f"Components:")
        for component in electrolyte['components']:
            st.text('Concentration:')
            if hasattr(component, 'name'):
                st.text(f"- Name: {component['name']}")
            if hasattr(component, 'type'):
                st.text(f"- Type: {component['type']}")
            if hasattr(component, 'concentration'):
                if hasattr(component, 'unit'):
                    st.text(f"Unit: {component['concentration']['unit']}")
                if hasattr(component, 'value'):
                    st.text(f"Value: {component['concentration']['value']}")
               
        try:
            temp_unit=electrochemical_system["electrolyte"]["temperature"]["unit"]
            temp_value=electrochemical_system["electrolyte"]["temperature"]["value"]
            if temp_unit or temp_value:
                st.text(f"Temperature:")
            if temp_unit:
                st.text(f"Unit: {temp_unit}")
            if temp_value:
                st.text(f"Value: {temp_value}")
        except:
            print("No temperature found")

        try:
            scan_rate = entry.figure_description['scan rate']
            st.subheader("Scan rate")
            if hasattr(scan_rate, 'unit'):
                st.text(f"Unit: {scan_rate['unit']}")       
            if hasattr(scan_rate, 'value'):
                st.text(f"Value: {scan_rate['value']}")
        except: 
            print("No scan rate")

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
