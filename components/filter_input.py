import streamlit as st
from components.icon_button import IconButton, IconType


def FilterInput():

    for index, filter_state in enumerate(st.session_state["filter"]):

        if index == 0:
            col1, col2, col3, _ = st.columns([2, 2, 2, 1])

            with col1:
                st.write("Column")
            with col2:
                st.write("Operator")
            with col3:
                st.write("Value")

        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])

        with col1:
            column_input = st.selectbox(
                "Column",
                ("Material", "Orientation", "Electrolyte", "Year"),
                key=f"col-sel-input-{index}",
                label_visibility="collapsed",
            )

        with col2:
            operator_input = st.selectbox(
                "Operator",
                (
                    "contains",
                    "not contains",
                    "equals",
                    "not equals",
                    "starts with",
                    "ends with",
                    "is empty",
                    "is not empty",
                ),
                key=f"op-sel-input-{index}",
                label_visibility="collapsed",
            )

        with col3:
            value_input = ""
            if operator_input != "is empty" and operator_input != "is not empty":
                value_input = st.text_input(
                    "Value", key=f"val-txt-input-{index}", label_visibility="collapsed"
                )

        with col4:
            IconButton(
                IconType.TRASH,
                f"button-trash-icon-{index}",
                on_click=lambda: remove_filter(index),
            )

        st.session_state["filter"][index] = {
            "column": column_input,
            "operator": operator_input,
            "value": value_input,
        }

    IconButton(
        IconType.FILTER,
        "new-filter-button",
        on_click=new_filter,
        text="New Filter",
        padding_right="5px",
    )


def new_filter():
    st.session_state["filter"].append({"column": "", "operator": "", "value": ""})


def remove_filter(index):
    st.session_state["filter"].pop(index)
