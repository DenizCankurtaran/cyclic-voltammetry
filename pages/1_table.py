from db.entries import get_entries_with_materials_and_system_type
from components.filter_input import FilterInput
from components.nav_bar import NavBar
from components.icon_button import IconStyleSheet
from util.operator import apply_operator
from util.electrode import create_we_electrode, get_electrolyte_composition
from util.source import create_source
from util.get_thumbnail import get_thumbnail
from util.pages import GRAPH_PAGE
import streamlit as st
import pandas as pd
import frictionless

NavBar("Table")


IconStyleSheet()

if "materials" not in st.session_state:
    st.session_state["materials"] = ""

if "system" not in st.session_state:
    st.session_state["system"] = ""

if "filter" not in st.session_state:
    st.session_state["filter"] = []

materials = st.session_state["materials"].split(" ")

system_type = st.session_state["system"]


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

        graph_thumbnail = get_thumbnail(entry)
        table_entries.append(
            {
                "name": entry.package.resource_names[0],  # used to get db entry
                "graph": graph_thumbnail,
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
    selected_table_entries_indices = st.session_state["selected_plots"]["selection"][
        "rows"
    ]
    selected_table_entries = [
        filtered_table_entries[index] for index in selected_table_entries_indices
    ]
    selected_entries = [
        entries[table_entry["name"]] for table_entry in selected_table_entries
    ]
    st.session_state["multiplot"] = selected_entries


FilterInput()

entries_with_materials_and_system_type = get_entries_with_materials_and_system_type(
    materials, system_type
)

table_entries = get_table_entries(entries_with_materials_and_system_type)
filtered_entries = list(filter(lambda x: apply_filter_input(x), table_entries))

if st.button("Plot"):
    set_multiplot_state(filtered_entries, entries_with_materials_and_system_type)
    st.switch_page(GRAPH_PAGE)

df = pd.DataFrame(filtered_entries)
st.dataframe(
    df,
    height=(len(filtered_entries) + 1) * 35 + 3,
    on_select="rerun",
    selection_mode="multi-row",
    use_container_width=True,
    column_config={
        "material": "Material",
        "orientation": "Orientation",
        "electrolyte": "Electrolyte",
        "year": "Year",
        "graph": st.column_config.ImageColumn("Graph"),
        "reference": st.column_config.LinkColumn("Reference", display_text="article"),
    },
    hide_index=True,
    column_order=[
        "graph",
        "material",
        "orientation",
        "electrolyte",
        "year",
        "reference",
    ],
    key="selected_plots",
)
