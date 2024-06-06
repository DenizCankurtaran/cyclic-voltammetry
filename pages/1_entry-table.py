from db.entries import get_entries, filter_Ag100Br
import streamlit as st
import pandas as pd

entries = get_entries(filter_Ag100Br)
df = pd.DataFrame(
    [
        {
            "Name": entry.package.resource_names[0],
            "Material": "",
            "Orientation": "",
            "Electrolyte": "",
            "Year": "",
            "Reference": "",
        }
        for entry in entries
    ]
)

st.dataframe(df, use_container_width=True)
