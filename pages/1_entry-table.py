from db.entries import get_entries_with_material
from components.filter_input import FilterInput
from util.operator import apply_operator
from util.electrode import (
    create_we_electrode,
    create_ce_electrode,
    create_ref_electrode,
)
import streamlit as st
import pandas as pd

if "filter" not in st.session_state:
    st.session_state["filter"] = []


material = "Ag"


def get_table_entries(entries):
    table_entries = []
    for entry in entries:
        t_unit = entry.field_unit("t")
        e_unit = entry.field_unit("E")
        try:
            j_unit = entry.field_unit("j")
        except frictionless.exception.FrictionlessException as e:
            j_unit = "A / m2"

        scanrate_value = entry.figure_description.scan_rate.value
        scanrate_unit = entry.figure_description.scan_rate.unit

        electrolyte = entry.system.electrolyte.__dict__["_descriptor"]

        try:
            we_electrode = create_we_electrode(
                entry.get_electrode("WE").__dict__["_descriptor"]
            )
        except KeyError:
            print("no WE electrode existing")

        try:
            ref_electrode = create_ref_electrode(
                entry.get_electrode("REF").__dict__["_descriptor"]
            )
        except KeyError:
            print("no REF electrode existing")

        try:
            ce_electrode = create_ce_electrode(
                entry.get_electrode("CE").__dict__["_descriptor"]
            )
        except KeyError:
            print("no CE electrode existing")

        table_entries.append(
            {
                "name": entry.package.resource_names[0],
                "material": we_electrode["name"],
                "orientation": we_electrode["crystallographicOrientation"],
                "electrolyte": "",
                "year": "",  # entry.bibliography['year'],
                "reference": "",
            }
        )
    return table_entries


def apply_filter_input(entries):
    if not entries:
        return []

    filtered_entries = entries.copy()
    for filter_state in st.session_state["filter"]:

        operator = filter_state["operator"]
        value = filter_state["value"]

        print(filter_state)
        if filter_state["column"] == "Name":
            filtered_entries = [
                entry
                for entry in filtered_entries
                if apply_operator(operator, entry["name"], value)
            ]

        if filter_state["column"] == "Material":
            filtered_entries = [
                entry
                for entry in filtered_entries
                if apply_operator(operator, entry["material"], value)
            ]
    return filtered_entries


FilterInput()

entries_with_material = get_entries_with_material(material)

table_entries = get_table_entries(entries_with_material)
filtered_entries = apply_filter_input(table_entries)

df = pd.DataFrame(filtered_entries)
st.dataframe(df, use_container_width=True)
