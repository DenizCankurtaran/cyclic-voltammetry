import streamlit as st
from components.element_button import ElementButton


# 90 Buttons
# Color with Css
def PeriodicTable(all_materials):

    elements = [
        ["H",  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "He"],
        ["Li", "Be", None, None, None, None, None, None, None, None, None, None, "B",  "C",  "N",  "O",  "F",  "Ne"],
        ["Na", "Mg", None, None, None, None, None, None, None, None, None, None, "Al", "Si", "P",  "S",  "Cl", "Ar"],
        ["K",  "Ca", "Sc", "Ti", "V",  "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
        ["Rb", "Sr", "Y",  "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I",  "Xe"],
        ["Cs", "Ba", "La", "Hf", "Ta", "W",  "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
        ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
    ]

    for row in elements:
        cols = st.columns(18)
        for i, element in enumerate(row):
            if element:
                with cols[i]:
                    ElementButton(element, all_materials)
