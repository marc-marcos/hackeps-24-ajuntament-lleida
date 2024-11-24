import streamlit as st
import pandas as pd
import numpy as np
from graphics_library import get_raw_data

st.title("Historial de vehicles")

if "id_parking" not in st.session_state:
    st.session_state.id_parking = 1

id = st.session_state.id_parking

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

st.table(df)