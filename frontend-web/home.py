import streamlit as st

st.title("Home")

if 'id_parking' not in st.session_state:
        st.session_state.id_parking = 1
