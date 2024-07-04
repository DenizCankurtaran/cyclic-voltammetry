import streamlit as st
from streamlit_navigation_bar import st_navbar
from util.pages import HOME_PAGE, TABLE_PAGE, ABOUT_PAGE


def NavBar(current_page):

    pages = ["Echemdb.org", "About", "GitHub"]
    if current_page in ["Table", "Graph"]:
        pages.insert(0, "Back")

    page = st_navbar(
        pages,
        logo_path="./assets/echemdb_logo.svg",
        selected=None,
        urls={
            "Echemdb.org": "https://www.echemdb.org/",
            "GitHub": "https://github.com/echemdb",
        },
        styles={
            "nav": {"background-color": "#006c67"},
            "ul": {"justify-content": "space-around"},
            "span": {"color": "white"},
            "div": {"max-width": "100%"},
        },
        options={"show_menu": False},
    )

    if current_page != "Home" and page == "Home":
        st.switch_page(HOME_PAGE)
    if page == "About":
        st.switch_page(ABOUT_PAGE)
    if page == "Back":
        if current_page == "Table":
            st.switch_page(HOME_PAGE)
        if current_page == "Graph":
            st.switch_page(TABLE_PAGE)
