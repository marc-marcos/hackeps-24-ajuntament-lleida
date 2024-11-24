import streamlit as st
from contants import BASE_URL
import requests
import random
import json


def create_parking_and_planta(nombre, latitude, longitude, accesible):
    # URL for the POST request
    url = f"http://{BASE_URL}:8000/api/parking/"  # Replace with your actual endpoint

    # Data to send in the POST request
    data = {
        "latitude": latitude,
        "longitude": longitude,
        "nom": nombre,
        "accesible": accesible,
    }

    # Headers (optional, but typical for JSON data)
    headers = {"Content-Type": "application/json"}

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response
    if response.status_code == 200 or response.status_code == 201:
        print(f"Request was successful {response.json()["id"]}")

        id = response.json()["id"]

        # Crear una planta

        data = {"nom": "Planta 1", "parking": id}

        response = requests.post(
            f"http://{BASE_URL}:8000/api/planta/",
            headers=headers,
            data=json.dumps(data),
        )

        if response.status_code == 200 or response.status_code == 201:
            print(f"Request was successful {response.json()["id"]}")
            id_planta = response.json()["id"]
            # Crear diez plazas
            for i in range(10):
                ocupada = random.choice([True, False])

                data = {"ocupada": ocupada, "planta": id_planta}
                response = requests.post(
                    f"http://{BASE_URL}:8000/api/plaza/",
                    headers=headers,
                    data=json.dumps(data),
                )
                if response.status_code == 200 or response.status_code == 201:
                    print(f"Request was successful {response.json()["id"]}")

                else:
                    print(
                        f"Request failed with status code {response.status_code}: {response.text}"
                    )

    else:
        print(
            f"Request failed with status code {response.status_code}: {response.text}"
        )


st.set_page_config(
    page_title="Your App Title",
    page_icon="logo.png",  # Emoji or small image path
    layout="wide",
)


def process_inputs(input1, input2, input3):
    st.success(f"Processed inputs: {input1}, {input2}, {input3}")


st.sidebar.image("logo.png", use_container_width=True)

st.title("Manage")

st.header("Afegir un nou parking")

with st.form("my_form"):
    nom = st.text_input("Nom del parking:")
    longitude = st.number_input(
        label="Enter a number",
        min_value=0.0,  # Optional: Minimum value
        max_value=100.0,  # Optional: Maximum value
        value=10.0,  # Default value
        step=1.0,  # Step size
        format="%f",  # Format (e.g., %d for integer, %f for float)
        key="longitude",
    )
    latitude = st.number_input(
        label="Enter a number",
        min_value=0.0,  # Optional: Minimum value
        max_value=100.0,  # Optional: Maximum value
        value=10.0,  # Default value
        step=1.0,  # Step size
        format="%f",  # Format (e.g., %d for integer, %f for float)
        key="latitude",
    )

    active = st.checkbox(
        "És el parking accessible per a persones amb movilitat reduida?", value=False
    )

    # Submit button
    submit_button = st.form_submit_button(label="Submit")

# Trigger function if the form is submitted
if submit_button:
    create_parking_and_planta(nom, float(latitude), float(longitude), active)
