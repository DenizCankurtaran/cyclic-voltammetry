import streamlit as st
from components.element_button import ElementButton


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
