import streamlit as st

#90 Buttons
#Color with Css
def PeriodicTable():

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 = st.columns(18)

    with col1:
        st.button("H")
        st.button("Li")
        st.button("Na")
        st.button("K")
        st.button("Rb")
        st.button("Cs")
        st.button("Fr")
    with col2:
        st.button("Be")
        st.button("Mg")
        st.button("Ca")
        st.button("Sr")
        st.button("Ba")
        st.button("Ra")
    with col3:
        st.button("Sc")
        st.button("Y")
        st.button("La")
        st.button("Ac")
    with col4:
        st.button("Ti")
        st.button("Zr")
        st.button("Hf")
        st.button("Rf")
    with col5:
        st.button("V")
        st.button("Nb")
        st.button("Ta")
        st.button("Db")
    with col6:
        st.button("Cr")
        st.button("Mo")
        st.button("W")
        st.button("Sg")
    with col7:
        st.button("Mn")
        st.button("Tc")
        st.button("Re")
        st.button("Bh")
    with col8:
        st.button("Fe")
        st.button("Ru")
        st.button("Os")
        st.button("Hs")
    with col9:
        st.button("Co")
        st.button("Rh")
        st.button("Ir")
        st.button("Mt")
    with col10:
        st.button("Ni")
        st.button("Pd")
        st.button("Pt")
        st.button("Ds")
    with col11:
        st.button("Cu")
        st.button("Ag")
        st.button("Au")
        st.button("Rg")
    with col12:
        st.button("Zn")
        st.button("Cd")
        st.button("Hg")
        st.button("Cn")
    with col13:
        st.button("B")
        st.button("Al")
        st.button("Ga")
        st.button("In")
        st.button("Tl")
        st.button("Nh")
    with col14:
        st.button("C")
        st.button("Si")
        st.button("Ge")
        st.button("Sn")
        st.button("Pb")
        st.button("Fl")
    with col15:
        st.button("N")
        st.button("P")
        st.button("As")
        st.button("Sb")
        st.button("Bi")
        st.button("Mc")
    with col16:
        st.button("O")
        st.button("S")
        st.button("Se")
        st.button("Te")
        st.button("Po")
        st.button("Lv")
    with col17:
        st.button("F")
        st.button("Cl")
        st.button("Br")
        st.button("I")
        st.button("At")
        st.button("Ts")
    with col18:
        st.button("He")
        st.button("Ne")
        st.button("Ar")
        st.button("Kr")
        st.button("Xe")
        st.button("Rn")
        st.button("Og")