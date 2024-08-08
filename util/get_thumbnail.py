import base64
import streamlit as st


@st.cache_data
def get_thumbnail(_entry, name):
    """
    entry.thumbnail() does not return consistent binary code.
    This creates a different binary code is inperpreted as a intentional change
    causing a reload of the page and unselecting previous selected entries in the table.

    This is solved for now, by caching the thumbnail with the identifier "name".
    The entry itself is not cached because of the underscore "_".
    """
    base64_image = base64.b64encode(_entry.thumbnail()).decode("utf-8")
    return f"data:image/png;base64,{base64_image}"
