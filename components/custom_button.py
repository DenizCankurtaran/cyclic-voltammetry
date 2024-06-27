import streamlit as st

def custom_button(label, on_click=None, args=None, css=None):
    button_id = f"button-{label}"
    if css is None:
        css = {
            "color": "black",
            "background-color": "white",
            "border": "1px solid black",
            "padding": "10px",
            "border-radius": "5px",
            "cursor": "pointer",
        }

    button_style = "; ".join([f"{k}: {v}" for k, v in css.items()])

    button_html = f"""
    <button id="{button_id}" style="{button_style}" onclick="{on_click}">{label}</button>
    
    """

    st.markdown(button_html, unsafe_allow_html=True)

