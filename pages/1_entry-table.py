from db.entries import get_entries, filter_Ag100Br
import streamlit as st
import pandas as pd


def get_table_entry_data(entry):
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

    return {
        "name": entry.package.resource_names[0],
        "material": we_electrode["name"],
        "orientation": we_electrode["crystallographicOrientation"],
        "electrolyte": "",
        "year": "",  # entry.bibliography['year'],
        "reference": "",
    }


def create_ce_electrode(ce):
    ce_electrode = dict()
    ce_electrode["name"] = ce["name"]
    ce_electrode["function"] = ce["function"]
    ce_electrode["material"] = ce["material"]
    if "crystallographic orientation" in ce:
        ce_electrode["crystallographicOrientation"] = ce["crystallographic orientation"]
    if "supplier" in ce:
        ce_electrode["supplier"] = ce["supplier"]
    if "shape" in ce:
        ce_electrode["shape"] = ce["shape"]
    return ce_electrode


def create_ref_electrode(ref):
    ref_electrode = dict()
    ref_electrode["name"] = ref["name"]
    ref_electrode["function"] = ref["function"]
    if "source" in ref:
        if "supplier" in ref["source"]:
            ref_electrode["source"] = ref["source"]["supplier"]
        else:
            ref_electrode["source"] = ref["source"]
    if "supplier" in ref:
        ref_electrode["supplier"] = ref["supplier"]
    if "type" in ref:
        ref_electrode["type"] = ref["type"]
    return ref_electrode


def create_we_electrode(we):
    we_electrode = dict()
    we_electrode["name"] = we["name"]
    we_electrode["function"] = we["function"]
    we_electrode["material"] = we["material"]
    we_electrode["crystallographicOrientation"] = we["crystallographic orientation"]
    if "geometric electrolyte contact area" in we:
        we_electrode["geometricElectrolyteContactArea"] = we[
            "geometric electrolyte contact area"
        ]["unit"]
    if "shape" in we:
        we_electrode["shape"] = we["shape"]
    if "source" in we:
        we_electrode["source"] = we["source"]
    return we_electrode


entries = get_entries(filter_Ag100Br)
# entries["endo_1999_in-situ_19_f1_a"].field_unit("j")
df = pd.DataFrame([get_table_entry_data(entry) for entry in entries])

st.dataframe(df, use_container_width=True)
