import requests
import random
import json

BASE_URL = "http://127.0.0.1:8000/api/"

# URL for the POST request
url = f"{BASE_URL}parking/"  # Replace with your actual endpoint

# Data to send in the POST request
data = {"latitude": 23.0, "longitude": 32.0, "nom": "Parking de la FIB"}


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
        f"{BASE_URL}planta/", headers=headers, data=json.dumps(data)
    )

    if response.status_code == 200 or response.status_code == 201:
        print(f"Request was successful {response.json()["id"]}")
        id_planta = response.json()["id"]
        # Crear diez plazas
        for i in range(10):
            ocupada = random.choice([True, False])

            data = {"ocupada": ocupada, "planta": id_planta}
            response = requests.post(
                f"{BASE_URL}plaza/", headers=headers, data=json.dumps(data)
            )
            if response.status_code == 200 or response.status_code == 201:
                print(f"Request was successful {response.json()["id"]}")

            else:
                print(
                    f"Request failed with status code {response.status_code}: {response.text}"
                )


else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
