import streamlit as st
from components.periodic_table import PeriodicTable
from components.nav_bar import NavBar
from components.icon_button import IconButton, IconType, IconStyleSheet
from util.pages import TABLE_PAGE
from db.entries import get_all_entries

st.set_page_config(layout="wide")
NavBar("Home")

IconStyleSheet()

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    .subheader {
        text-align: center;
        color: #888888;
        margin-bottom: 30px;
    }
    .header {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="title">Welcome to echemdb</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheader">The community database for electrochemical data</h2>', unsafe_allow_html=True)

if "materials" not in st.session_state:
    st.session_state["materials"] = ""


if "system" not in st.session_state:
    st.session_state["system"] = "aqueous"

materials = st.session_state["materials"]


search_bar, select_system, search_button = st.columns([4, 1, 1])

all_entries = get_all_entries()

with search_bar:
    search_bar_value = st.text_input(
        label="Element Input",
        placeholder="Type in or click the element(s) you are looking for",
        label_visibility="collapsed",
        value=materials,
    )
    st.session_state["materials"] = search_bar_value

with select_system:
    select_system_value = st.selectbox(
        "System",
        [
            "Aqueous",
            "Non aqueous",
        ],
        index=0,
        label_visibility="collapsed",
    )
    if select_system_value == "Aqueous":
        st.session_state["system"] = "aqueous"
    else:
        st.session_state["system"] = "ionic liquid"


with search_button:
    if IconButton(
        IconType.SEARCH,
        "search-button",
        text="Search",
        padding_right="5px",
    ):
        st.switch_page(TABLE_PAGE)


PeriodicTable(all_entries.materials())

st.markdown('<h3 class="header">Project developed through the collaboration of:</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("util/images/logo_fhi.png", use_column_width=True)
with col2:
    st.image("util/images/logo_bht.png", use_column_width=True)
with col3:
    st.image("util/images/logo_ulm.png", use_column_width=True)