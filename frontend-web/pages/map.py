import streamlit as st
import pandas as pd
import numpy as np
import requests as req
import folium
from streamlit_folium import folium_static

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
    
    folium_map = folium.Map(location=[latitud_catalunya, longitud_catalunya], zoom_start=10)

    for parquing in parquings:
        id = st.session_state.id_parking
        url = f'http://127.0.0.1:8000/api/parking/{id}/plazas'
        response = req.get(url)

        if response.status_code == 200:
            data2 = response.json()
            ocuppied = [item["ocupada"] for item in data2]
            plazas = 0
            for ocup in ocuppied:
                if not ocup:
                    plazas += 1
            if (plazas > 0): colorPoint = "#008000"

            folium.Marker(
                location=[parquing['latitude'], parquing['longitude']],
                popup=f"{parquing['nom']}<br><br>Places disponibles: {plazas}<br><br>{'Accesible' if parquing['accesible'] else 'No accesible'}"
                icon=folium.Icon(color=colorPoint)
            ).add_to(folium_map)

        else: st.error("Error al carregar les places del pàrquing")
    folium_static(folium_map)
else: st.error("Error al carregar els pàrquings")

