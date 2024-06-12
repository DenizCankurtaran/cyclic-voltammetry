import streamlit as st


def FilterInput():

    for index, filter_state in enumerate(st.session_state["filter"]):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.button(
                "x", on_click=lambda: remove_filter(index), key=f"remove-btn-{index}"
            )

        with col2:
            column_input = st.selectbox(
                "Column",
                ("Name", "Material", "Orientation", "Electrolyte", "Year"),
                key=f"col-sel-input-{index}",
            )

        with col3:
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
            )

        with col4:
            value_input = ""
            if operator_input != "is empty" and operator_input != "is not empty":
                value_input = st.text_input("Value", key=f"val-txt-input-{index}")

        st.session_state["filter"][index] = {
            "column": column_input,
            "operator": operator_input,
            "value": value_input,
        }

    col1, col2 = st.columns(2)
    with col1:
        st.button("New", on_click=new_filter)

    with col2:
        st.button("Remove", on_click=remove_all_filter)


def new_filter():
    st.session_state["filter"].append({"column": "", "operator": "", "value": ""})


def remove_all_filter():
    st.session_state["filter"] = []


def remove_filter(index):
    st.session_state["filter"].pop(index)
