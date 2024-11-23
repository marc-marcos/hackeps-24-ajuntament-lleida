import streamlit as st
import pandas as pd
import numpy as np
import requests as req

# Coordenadas aproximadas del centro de Cataluña (Barcelona)
latitud_catalunya = 41.5963
longitud_catalunya = 1.4744

# Crear un DataFrame con las coordenadas
data = pd.DataFrame({
    'latitude': [latitud_catalunya],
    'longitude': [longitud_catalunya],
    'zoom': [150],
    'name': ['Catalunya'],
    'size': [40]
})

st.title("Localitza un pàrquing")
st.map(data)

