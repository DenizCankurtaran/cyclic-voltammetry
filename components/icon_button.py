import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import os
from enum import Enum


class IconType(Enum):
    TRASH = 0
    SEARCH = 1
    FILTER = 2


def get_icon_unicode(icon_type):
    if icon_type == IconType.TRASH:
        return r"\f1f8"
    if icon_type == IconType.SEARCH:
        return r"\f002"
    if icon_type == IconType.FILTER:
        return r"\f0b0"


def IconButton(icon_type, button_id, on_click=None, text="", padding_right="0"):
    """
    Component to use has to inject css

    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"/>',
        unsafe_allow_html=True,
    )
    """

    icon_unicode = get_icon_unicode(icon_type)

    main_container_tag = "p" if text else "div"
    reset_container_tag = "div" if text else "p"

    icon_css = f"font-family: 'Font Awesome 5 Free'; content: '{icon_unicode}'; display: inline-block; vertical-align: middle; font-weight: 900; padding-right: {padding_right}"

    with stylable_container(
        key=f"container-{button_id}",
        css_styles=f"button {main_container_tag}:before"
        + "{"
        + icon_css
        + "}"
        + f"button {reset_container_tag}:before"
        + "{}",
    ):
        st.button(text, on_click=on_click, key=button_id)
