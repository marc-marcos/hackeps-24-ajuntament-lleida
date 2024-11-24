import streamlit as st

st.set_page_config(
    page_title="Your App Title",
    page_icon="logo.png",  # Emoji or small image path
    layout="wide",
)

st.sidebar.image("logo.png", use_container_width=True)

st.title("Home")

if "id_parking" not in st.session_state:
    st.session_state.id_parking = 1
