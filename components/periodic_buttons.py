import streamlit as st
from components.custom_button import custom_button

def select_element(element):
    materials = st.session_state.get("materials", "")
    if not materials:
        materials = f"{element}"
    else:
        materials = f"{materials} {element}"
    st.session_state["materials"] = materials

noble_gases_css = {
    "background-color": "#AC1258",
    "color": "white",
    "border": "1px solid black",
    "padding": "10px",
    "border-radius": "5px",
    "cursor": "pointer",
}

reactive_nonmetal_css = {
    "background-color": "#3E50B5",
    "color": "white",
    "border": "1px solid black",
    "padding": "10px",
    "border-radius": "5px",
    "cursor": "pointer",
}  

def PeriodicTable():
    st.title("Interactive Periodic Table")
    
    # Layout the first row
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)
    
    with col1:
        custom_button("H", on_click=select_element, args="H",css=reactive_nonmetal_css)
    with col18:
        custom_button("He", on_click=select_element, args="He",css=noble_gases_css)
    
    # Layout the second row
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)
    
    with col1:
        st.button("Li", on_click=select_element, args=("Li",))
        
        #m = st.markdown("""
        #<style>
        #div.stButton > button:first-child {
        #    background-color: rgb(204, 49, 49);
        #}
        #</style>""", unsafe_allow_html=True)
        #b = st.button("Li", on_click=select_element, args=("Li",))

    with col2:
        st.button("Be", on_click=select_element, args=("Be",))
    with col13:
        st.button("B", on_click=select_element, args=("B",))
    with col14:
        st.button("C", on_click=select_element, args=("C",))
    with col15:
        st.button("N", on_click=select_element, args=("N",))
    with col16:
        st.button("O", on_click=select_element, args=("O",))
    with col17:
        st.button("F", on_click=select_element, args=("F",))
    with col18:
        st.button("Ne", on_click=select_element, args=("Ne",))
    
    # Layout the third row
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)
    
    with col1:
        st.button("Na", on_click=select_element, args=("Na",))
    with col2:
        st.button("Mg", on_click=select_element, args=("Mg",))
    with col13:
        st.button("Al", on_click=select_element, args=("Al",))
    with col14:
        st.button("Si", on_click=select_element, args=("Si",))
    with col15:
        st.button("P", on_click=select_element, args=("P",))
    with col16:
        st.button("S", on_click=select_element, args=("S",))
    with col17:
        st.button("Cl", on_click=select_element, args=("Cl",))
    with col18:
        st.button("Ar", on_click=select_element, args=("Ar",))
    
    # Layout the fourth row
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)
    
    with col1:
        st.button("K", on_click=select_element, args=("K",))
    with col2:
        st.button("Ca", on_click=select_element, args=("Ca",))
    with col3:
        st.button("Sc", on_click=select_element, args=("Sc",))
    with col4:
        st.button("Ti", on_click=select_element, args=("Ti",))
    with col5:
        st.button("V", on_click=select_element, args=("V",))
    with col6:
        st.button("Cr", on_click=select_element, args=("Cr",))
    with col7:
        st.button("Mn", on_click=select_element, args=("Mn",))
    with col8:
        st.button("Fe", on_click=select_element, args=("Fe",))
    with col9:
        st.button("Co", on_click=select_element, args=("Co",))
    with col10:
        st.button("Ni", on_click=select_element, args=("Ni",))
    with col11:
        st.button("Cu", on_click=select_element, args=("Cu",))
    with col12:
        st.button("Zn", on_click=select_element, args=("Zn",))
    with col13:
        st.button("Ga", on_click=select_element, args=("Ga",))
    with col14:
        st.button("Ge", on_click=select_element, args=("Ge",))
    with col15:
        st.button("As", on_click=select_element, args=("As",))
    with col16:
        st.button("Se", on_click=select_element, args=("Se",))
    with col17:
        st.button("Br", on_click=select_element, args=("Br",))
    with col18:
        st.button("Kr", on_click=select_element, args=("Kr",))

    # Layout the fifth row
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)
    
    with col1:
        st.button("Rb", on_click=select_element, args=("Rb",))
    with col2:
        st.button("Sr", on_click=select_element, args=("Sr",))
    with col3:
        st.button("Y", on_click=select_element, args=("Y",))
    with col4:
        st.button("Zr", on_click=select_element, args=("Zr",))
    with col5:
        st.button("Nb", on_click=select_element, args=("Nb",))
    with col6:
        st.button("Mo", on_click=select_element, args=("Mo",))
    with col7:
        st.button("Tc", on_click=select_element, args=("Tc",))
    with col8:
        st.button("Ru", on_click=select_element, args=("Ru",))
    with col9:
        st.button("Rh", on_click=select_element, args=("Rh",))
    with col10:
        st.button("Pd", on_click=select_element, args=("Pd",))
    with col11:
        st.button("Ag", on_click=select_element, args=("Ag",))
    with col12:
        st.button("Cd", on_click=select_element, args=("Cd",))
    with col13:
        st.button("In", on_click=select_element, args=("In",))
    with col14:
        st.button("Sn", on_click=select_element, args=("Sn",))
    with col15:
        st.button("Sb", on_click=select_element, args=("Sb",))
    with col16:
        st.button("Te", on_click=select_element, args=("Te",))
    with col17:
        st.button("I", on_click=select_element, args=("I",))
    with col18:
        st.button("Xe", on_click=select_element, args=("Xe",))

    # Layout the sixth row
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)
    
    with col1:
        st.button("Cs", on_click=select_element, args=("Cs",))
    with col2:
        st.button("Ba", on_click=select_element, args=("Ba",))
    with col3:
        st.button("La", on_click=select_element, args=("La",))
    with col4:
        st.button("Hf", on_click=select_element, args=("Hf",))
    with col5:
        st.button("Ta", on_click=select_element, args=("Ta",))
    with col6:
        st.button("W", on_click=select_element, args=("W",))
    with col7:
        st.button("Re", on_click=select_element, args=("Re",))
    with col8:
        st.button("Os", on_click=select_element, args=("Os",))
    with col9:
        st.button("Ir", on_click=select_element, args=("Ir",))
    with col10:
        st.button("Pt", on_click=select_element, args=("Pt",))
    with col11:
        st.button("Au", on_click=select_element, args=("Au",))
    with col12:
        st.button("Hg", on_click=select_element, args=("Hg",))
    with col13:
        st.button("Tl", on_click=select_element, args=("Tl",))
    with col14:
        st.button("Pb", on_click=select_element, args=("Pb",))
    with col15:
        st.button("Bi", on_click=select_element, args=("Bi",))
    with col16:
        st.button("Po", on_click=select_element, args=("Po",))
    with col17:
        st.button("At", on_click=select_element, args=("At",))
    with col18:
        st.button("Rn", on_click=select_element, args=("Rn",))
    
    # Layout the seventh row
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)
    
    with col1:
        st.button("Fr", on_click=select_element, args=("Fr",))
    with col2:
        st.button("Ra", on_click=select_element, args=("Ra",))
    with col3:
        st.button("Ac", on_click=select_element, args=("Ac",))
    with col4:
        st.button("Rf", on_click=select_element, args=("Rf",))
    with col5:
        st.button("Db", on_click=select_element, args=("Db",))
    with col6:
        st.button("Sg", on_click=select_element, args=("Sg",))
    with col7:
        st.button("Bh", on_click=select_element, args=("Bh",))
    with col8:
        st.button("Hs", on_click=select_element, args=("Hs",))
    with col9:
        st.button("Mt", on_click=select_element, args=("Mt",))
    with col10:
        st.button("Ds", on_click=select_element, args=("Ds",))
    with col11:
        st.button("Rg", on_click=select_element, args=("Rg",))
    with col12:
        st.button("Cn", on_click=select_element, args=("Cn",))
    with col13:
        st.button("Nh", on_click=select_element, args=("Nh",))
    with col14:
        st.button("Fl", on_click=select_element, args=("Fl",))
    with col15:
        st.button("Mc", on_click=select_element, args=("Mc",))
    with col16:
        st.button("Lv", on_click=select_element, args=("Lv",))
    with col17:
        st.button("Ts", on_click=select_element, args=("Ts",))
    with col18:
        st.button("Og", on_click=select_element, args=("Og",))

if "materials" not in st.session_state:
    st.session_state["materials"] = ""
