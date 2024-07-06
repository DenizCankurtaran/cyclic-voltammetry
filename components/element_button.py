import streamlit as st


def select_element(*args):
    element = "".join(args)
    materials = st.session_state["materials"]
    if not materials:
        materials = f"{element}"
    else:
        materials = f"{materials} {element}"
    st.session_state["materials"] = materials


def ElementButton(element, all_materials):
    background_color = get_element_button_color(element)
    button_css = f"background-color: {background_color}; color: white; width: 40px; height: 40px; "
    disabled_button_css = f"background-color: {background_color}; opacity: 0.5;"
    p_css = f"word-break: keep-all"

    st.markdown(
        "<style>"
        + f".element-container:has(#button-{element}) + div button"
        + "{"
        + button_css
        + "}"
        + f".element-container:has(#button-{element}) + div button:disabled"
        + "{"
        + disabled_button_css
        + "}"
        + f".element-container:has(#button-{element}) + div button *"
        + "{"
        + p_css
        + "}"
        + "</style>"
        + f'<span id="button-{element}"></span>',
        unsafe_allow_html=True,
    )

    st.button(
        element,
        on_click=select_element,
        args=element,
        disabled=element not in all_materials,
    )


def get_element_button_color(element):
    if element in ["Li", "Na", "K", "Rb", "Cs", "Fr"]:
        return "#00766A"
    if element in ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"]:
        return "#C42529"
    if element in [
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
    ]:
        return "#691A98"
    if element in ["B", "Si", "Ge", "As", "Sb", "Te", "Po", "At"]:
        return "#817518"
    if element in ["H", "C", "N", "O", "P", "S", "Se"]:
        return "#3C4FB3"
    if element in ["F", "Cl", "Br", "I", "Ts"]:
        return "#3C4FB3"
    if element in ["He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og"]:
        return "#AA1258"
    if element in ["Al", "Ga", "In", "Sn", "Tl", "Pb", "Bi"]:
        return "#2C7A30"
    if element in [
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
    ]:
        return "#2391EB"
    if element in [
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
    ]:
        return "#745148"
    if element in ["Nh", "Fl", "Mc", "Lv", "Ts", "Og", "Ds", "Rg", "Cn"]:
        return "#5F5F5F"
