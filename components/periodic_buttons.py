import streamlit as st


def select_element(*args):
    element = "".join(args)
    materials = st.session_state["materials"]
    if not materials:
        materials = f"{element}"
    else:
        materials = f"{materials} {element}"
    st.session_state["materials"] = materials


# 90 Buttons
# Color with Css
def PeriodicTable(all_materials):
    (
        col1,
        col2,
        col3,
        col4,
        col5,
        col6,
        col7,
        col8,
        col9,
        col10,
        col11,
        col12,
        col13,
        col14,
        col15,
        col16,
        col17,
        col18,
    ) = st.columns(18)

    with col1:
        elements = ["H", "Li", "Na", "K", "Rb", "Cs", "Fr"]
        for element in elements:
            ElementButton(element, all_materials)
    with col2:
        elements = ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"]
        for element in elements:
            ElementButton(element, all_materials)
    with col3:
        elements = ["Sc", "Y", "La", "Ac"]
        for element in elements:
            ElementButton(element, all_materials)
    with col4:
        elements = ["Ti", "Zr", "Hf", "Rf"]
        for element in elements:
            ElementButton(element, all_materials)
    with col5:
        elements = ["V", "Nb", "Ta", "Db"]
        for element in elements:
            ElementButton(element, all_materials)
    with col6:
        elements = ["Cr", "Mo", "W", "Sg"]
        for element in elements:
            ElementButton(element, all_materials)
    with col7:
        elements = ["Mn", "Tc", "Re", "Bh"]
        for element in elements:
            ElementButton(element, all_materials)
    with col8:
        elements = ["Fe", "Ru", "Os", "Hs"]
        for element in elements:
            ElementButton(element, all_materials)
    with col9:
        elements = ["Co", "Rh", "Ir", "Mt"]
        for element in elements:
            ElementButton(element, all_materials)
    with col10:
        elements = ["Ni", "Pd", "Pt", "Ds"]
        for element in elements:
            ElementButton(element, all_materials)
    with col11:
        elements = ["Cu", "Ag", "Au", "Rg"]
        for element in elements:
            ElementButton(element, all_materials)
    with col12:
        elements = ["Zn", "Cd", "Hg", "Cn"]
        for element in elements:
            ElementButton(element, all_materials)
    with col13:
        elements = ["B", "Al", "Ga", "In", "Tl", "Nh"]
        for element in elements:
            ElementButton(element, all_materials)
    with col14:
        elements = ["C", "Si", "Ge", "Sn", "Pb", "Fl"]
        for element in elements:
            ElementButton(element, all_materials)
    with col15:
        elements = ["N", "P", "As", "Sb", "Bi", "Mc"]

        for element in elements:
            ElementButton(element, all_materials)
    with col16:
        elements = ["O", "S", "Se", "Te", "Po", "Lv"]
        for element in elements:
            ElementButton(element, all_materials)
    with col17:
        elements = ["F", "Cl", "Br", "I", "At", "Ts"]
        for element in elements:
            ElementButton(element, all_materials)

    with col18:
        elements = ["He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og"]
        for element in elements:
            ElementButton(element, all_materials)


def ElementButton(element, all_materials):
    background_color = getElementButtonColor(element)
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


def getElementButtonColor(element):
    button_colors = {
        "H": "#3C4FB3",
        "C": "#7280C3",
        "N": "#3C4FB3",
        "O": "#3C4FB3",
        "P": "#3C4FB3",
        "S": "#3C4FB3",
        "Se": "#3C4FB3",
        "F": "#3C4FB3",
        "Cl": "#3C4FB3",
        "Br": "#3C4FB3",
        "I": "#3C4FB3",
        "Li": "#00766A",
        "Na": "#00766A",
        "K": "#00766A",
        "Rb": "#00766A",
        "Cs": "#00766A",
        "Fr": "#00766A",
        "Be": "#C42529",
        "Mg": "#C42529",
        "Ca": "#C42529",
        "Sr": "#C42529",
        "Ba": "#C42529",
        "Ra": "#C42529",
        "La": "#2391EB",
        "Ac": "#745148",
        "He": "#AA1258",
        "Ne": "#AA1258",
        "Ar": "#AA1258",
        "Kr": "#AA1258",
        "Xe": "#AA1258",
        "Rn": "#AA1258",
        "B": "#817518",
        "Si": "#817518",
        "Ge": "#817518",
        "As": "#817518",
        "Sb": "#817518",
        "Te": "#817518",
        "At": "#817518",
        "Al": "#2C7A30",
        "Ga": "#2C7A30",
        "In": "#2C7A30",
        "Sn": "#2C7A30",
        "Tl": "#2C7A30",
        "Pb": "#2C7A30",
        "Bi": "#2C7A30",
        "Po": "#2C7A30",
        "Mt": "#5F5F5F",
        "Ds": "#5F5F5F",
        "Rg": "#5F5F5F",
        "Cn": "#5F5F5F",
        "Nh": "#5F5F5F",
        "Fl": "#5F5F5F",
        "Mc": "#5F5F5F",
        "Lv": "#5F5F5F",
        "Ts": "#5F5F5F",
        "Og": "#5F5F5F",
        "Sc": "#691A98",
        "Ti": "#691A98",
        "V": "#691A98",
        "Cr": "#691A98",
        "Mn": "#691A98",
        "Fe": "#691A98",
        "Co": "#691A98",
        "Ni": "#691A98",
        "Cu": "#691A98",
        "Zn": "#691A98",
        "Y": "#691A98",
        "Zr": "#691A98",
        "Nb": "#691A98",
        "Mo": "#691A98",
        "Tc": "#691A98",
        "Ru": "#691A98",
        "Rh": "#691A98",
        "Pd": "#691A98",
        "Ag": "#691A98",
        "Cd": "#691A98",
        "Hf": "#691A98",
        "Ta": "#691A98",
        "W": "#691A98",
        "Re": "#691A98",
        "Os": "#691A98",
        "Ir": "#691A98",
        "Pt": "#691A98",
        "Au": "#691A98",
        "Hg": "#691A98",
        "Rf": "#691A98",
        "Db": "#691A98",
        "Sg": "#691A98",
        "Bh": "#691A98",
        "Hs": "#691A98",
        # Add more elements and their colors as needed
    }
    return button_colors[element]
