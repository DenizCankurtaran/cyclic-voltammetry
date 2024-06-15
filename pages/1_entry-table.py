from db.entries import get_entries_with_material
from components.filter_input import FilterInput
from util.operator import apply_operator
from util.electrode import create_we_electrode, get_electrolyte_composition
from util.source import create_source
import streamlit as st
import pandas as pd
import base64


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

        electrolyte = get_electrolyte_composition(
            entry.system.electrolyte.__dict__["_descriptor"]
        )
        try:
            we_electrode = create_we_electrode(
                entry.get_electrode("WE").__dict__["_descriptor"]
            )
        except KeyError:
            # TODO: can this happen?
            we_electrode = {"material": ""}

        bibliography_year = ""
        if "year" in entry.bibliography.fields:
            bibliography_year = entry.bibliography.fields["year"]

        source = create_source(entry.source.__dict__["_descriptor"])

        encoded_image = base64.b64encode(entry.thumbnail()).decode("utf-8")
        table_entries.append(
            {
                "plot": False,
                "name": entry.package.resource_names[0],  # used to get db entry
                "graph": f"data:image/png;base64,{encoded_image}",
                "material": we_electrode["material"],
                "orientation": we_electrode["crystallographicOrientation"],
                "electrolyte": electrolyte,
                "year": bibliography_year,
                "reference": source["url"],
            }
        )
    return table_entries


def apply_filter_input(entry):
    matches = []
    for filter_state in st.session_state["filter"]:
        operator = filter_state["operator"]
        value = filter_state["value"]
        column_key = filter_state["column"].lower()
        if len(value) == 0:
            continue
        matches.append(apply_operator(operator, entry[column_key], value))
    return all(matches)


def set_multiplot_state(filtered_table_entries, entries):
    selected_table_entries_indices = [
        row_index
        for row_index in st.session_state["selected_plots"]["edited_rows"].keys()
    ]
    selected_table_entries = [
        filtered_entries[index] for index in selected_table_entries_indices
    ]
    selected_entries = [
        entries[table_entry["name"]] for table_entry in selected_table_entries
    ]
    st.session_state["multiplot"] = selected_entries


FilterInput()

entries_with_material = get_entries_with_material(material)

table_entries = get_table_entries(entries_with_material)
filtered_entries = list(filter(lambda x: apply_filter_input(x), table_entries))

df = pd.DataFrame(filtered_entries)
st.data_editor(
    df,
    use_container_width=True,
    column_config={
        "plot": st.column_config.CheckboxColumn("plot"),
        "graph": st.column_config.ImageColumn("graph"),
        "reference": st.column_config.LinkColumn("reference", display_text="article"),
    },
    hide_index=True,
    column_order=[
        "plot",
        "graph",
        "material",
        "orientation",
        "electrolyte",
        "year",
        "reference",
    ],
    disabled=[
        "graph",
        "material",
        "orientation",
        "electrolyte",
        "year",
        "reference",
    ],
    key="selected_plots",
)

if st.button("plot"):
    set_multiplot_state(filtered_entries, entries_with_material)
    st.switch_page("pages/2_graph.py")
