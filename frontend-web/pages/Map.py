import streamlit as st
import pandas as pd
import numpy as np
import requests as req
import folium
from streamlit_folium import st_folium
from contants import BASE_URL
# from streamlit_autorefresh import st_autorefresh

url = f"http://{BASE_URL}:8000/api/parking"

st.set_page_config(
    page_title="Your App Title",
    page_icon="logo.png",  # Emoji or small image path
    layout="wide",
)

st.sidebar.image("logo.png", use_container_width=True)

# Coordenadas aproximadas del centro de Cataluña (Barcelona)
latitud_catalunya = 41.5963
longitud_catalunya = 1.4744

if "selected_parking" not in st.session_state:
    st.session_state.selected_parking = None

# st_autorefresh(interval=2000)

parquings = req.get(url)

# valor per default null
data = pd.DataFrame(columns=["latitude", "longitude", "name", "size"])

st.title("Localitza un pàrquing")

if "id_parking" not in st.session_state:
    st.session_state.id_parking = 1

if parquings.status_code == 200:
    parquings = parquings.json()

    folium_map = folium.Map(
        location=[latitud_catalunya, longitud_catalunya], zoom_start=8
    )

    for parquing in parquings:
        id = parquing["id"]
        st.session_state.pk_clicked = "None"
        url = f"http://{BASE_URL}:8000/api/parking/{id}/plazas"
        response = req.get(url)

        if response.status_code == 200:
            data2 = response.json()
            ocuppied = [item["ocupada"] for item in data2]
            plazas = 0
            for ocup in ocuppied:
                if not ocup:
                    plazas += 1
            if plazas > 0:
                colorPoint = "green"
            else:
                colorPoint = "red"

            folium.Marker(
                location=[parquing["latitude"], parquing["longitude"]],
                popup=f"{parquing['nom']}<br><br>Places disponibles: {plazas}<br><br>{'Accesible' if parquing['accesible'] else 'No accesible'}<br><br>Ves-hi: <a href='https://www.google.com/maps/dir/{parquing['latitude']},{parquing['longitude']}'>Google Maps</a>",
                icon=folium.Icon(color=colorPoint),
            ).add_to(folium_map)
        else:
            st.error("Error al carregar les places del pàrquing")

    st_data = st_folium(folium_map, width=800, height=600)

    if st_data["last_object_clicked_popup"]:
        st.session_state.pk_clicked = st_data["last_object_clicked_popup"]

else:
    st.error("Error al carregar els pàrquings")


parquing_name = "None"
if st.session_state.pk_clicked != "None":
    # Extraer solo el nombre del párquing
    clicked_text = st.session_state.pk_clicked.splitlines()  # Divide en líneas
    parquing_name = clicked_text[0]  # La primera línea es el nombre
    st.write(f"{st.session_state.pk_clicked}")
else:
    st.write("Selecciona un pàrquing per veure les seves places disponibles")

# actualitza id
for parquing in parquings:
    if parquing["nom"] == parquing_name:  # Compara el nombre del parquing
        st.session_state.id_parking = parquing["id"]  # Asigna el ID al estado de sesión
        break  # Detén el bucle una vez encontrado el ID
