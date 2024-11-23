import streamlit as st
import pandas as pd
import numpy as np
import requests as req

url = "http://127.0.0.1:8000/api/parking"

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

parquings = req.get(url)

#valor per default null
data = pd.DataFrame(columns=['latitude', 'longitude', 'name', 'size'])
colorPoint = "#ff0000"
st.title("Localitza un pàrquing")

if 'id_parking' not in st.session_state:
    st.session_state.id_parking = 1

if parquings.status_code == 200:
    parquings = parquings.json()
    for parquing in parquings:
        id = st.session_state.id_parking
        url = f'http://127.0.0.1:8000/api/parking/{id}/plazas'
        response = req.get(url)
        data2 = response.json()
        ocuppied = [item["ocupada"] for item in data2]
        plazas = 0
        for ocup in ocuppied:
            if not ocup:
                plazas += 1
        if (plazas > 0): colorPoint = "#008000"
        data = data._append({
            'latitude': parquing['latitude'],
            'longitude': parquing['longitude'],
            'name': parquing['nom'],
            'size': 50 # tamaño de los marcadores

        }, ignore_index=True)
    
    st.map(data[['latitude', 'longitude']], zoom = 3, use_container_width=True, color = colorPoint)
else: st.error("Error al carregar els pàrquings")





