import streamlit as st
import time
import pandas as pd
import numpy as np
from graphics_library import get_raw_data

st.set_page_config(
    page_title="Your App Title",
    page_icon="logo.png",  # Emoji or small image path
    layout="wide",
)

st.sidebar.image("logo.png", use_container_width=True)

st.title("Historial de vehicles")

if "id_parking" not in st.session_state:
    st.session_state.id_parking = 1

id = st.session_state.id_parking


def fetch_data():
    df = get_raw_data()

    df["is_entrada"] = df["is_entrada"].map({True: "Entrada", False: "Sortida"})

    df.rename(
        columns={
            "is_entrada": "Tipus",
            "plaza": "Plaça",
            "id": "Identificador",
            "datahora": "Data i hora",
        },
        inplace=True,
    )

    df = df.drop(columns=["Identificador"])

    return df


placeholder = st.empty()

while True:
    df = fetch_data()
    with placeholder.container():
        st.table(df)

    time.sleep(5)
