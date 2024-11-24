import requests
import random
from datetime import datetime, timedelta
import json

BASE_URL = "http://127.0.0.1:8000/api/"


def create_init():
    # URL for the POST request
    url = f"{BASE_URL}parking/"  # Replace with your actual endpoint

    # Data to send in the POST request
    data = {
        "latitude": 23.0,
        "longitude": 32.0,
        "nom": "Parking de la FIB",
        "accesible": True,
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
        print(
            f"Request failed with status code {response.status_code}: {response.text}"
        )


def create_parking_and_planta(nombre, latitude, longitude, accesible):
    # URL for the POST request
    url = f"{BASE_URL}parking/"  # Replace with your actual endpoint

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
        print(
            f"Request failed with status code {response.status_code}: {response.text}"
        )


def flip_placa(id_placa):
    request = requests.get(f"{BASE_URL}plaza/{id_placa}/")

    data = request.json()

    if data["ocupada"]:
        nou_estat = False

    else:
        nou_estat = True

    data = {"ocupada": nou_estat}

    request = requests.patch(f"{BASE_URL}plaza/{id_placa}/", json=data)

    if request.status_code == 200:
        print("Request was successful")

    else:
        print(f"Request failed with status code {request.status_code}: {request.text}")

    return nou_estat


def update_placa(id_placa, nou_estat):
    data = {"ocupada": nou_estat}

    request = requests.patch(f"{BASE_URL}plaza/{id_placa}/", json=data)

    if request.status_code == 200:
        print("Request was successful")

    else:
        print(f"Request failed with status code {request.status_code}: {request.text}")


import requests
import random
from datetime import datetime, timedelta, timezone

# API endpoint
API_URL = "http://127.0.0.1:8000/api/plazalog/"


def get_number_of_plazas():
    response = requests.get("http://127.0.0.1:8000/api/plaza/")
    return len(response.json())


def get_planta_by_plaza(plaza):
    response = requests.get(f"http://127.0.0.1:8000/api/plaza/{plaza}/")
    return response.json()["planta"]


# Function to generate fake data
def generate_fake_data(timestamp):
    plaza_id = random.randint(1, get_number_of_plazas())

    planta = get_planta_by_plaza(plaza_id)

    is_entrada = flip_placa(plaza_id)

    return {
        "datahora": timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
        "plaza": plaza_id,
        "is_entrada": is_entrada,
    }


# Function to send logs
def send_log(log_data):
    try:
        response = requests.post(API_URL, json=log_data)
        response.raise_for_status()  # Raise an error for bad status codes
        print(f"Log sent successfully: {log_data}")
    except requests.RequestException as e:
        print(f"Failed to send log: {log_data} | Error: {e}")


# Main function
def fake_logs_for_day(date, min_interval_seconds=30, max_interval_seconds=300):
    start_time = datetime.combine(date, datetime.min.time(), tzinfo=timezone.utc)
    end_time = datetime.combine(date, datetime.max.time(), tzinfo=timezone.utc)

    current_time = start_time
    while current_time <= end_time:
        fake_data = generate_fake_data(current_time)
        send_log(fake_data)

        # Randomize the interval for the next log
        random_interval = random.randint(min_interval_seconds, max_interval_seconds)
        current_time += timedelta(seconds=random_interval)


if __name__ == "__main__":
    while True:
        print("Que vols fer? [Nomès una opció a la vegada]")
        print("1. Inicialitzar base de dades amb dummy data.")
        print("2. Flip plaça.")
        print("3. Generar dummy data.")
        print("4. Crear parking con init.")
        print("9. Exit.")

        a = input(">> ")

        if int(a) == 1:
            create_init()
        elif int(a) == 2:
            a = input("Quina plaça vols flipar? >> ")
            flip_placa(int(a))
        elif int(a) == 3:
            fake_date = datetime.strptime(
                "2024-11-22", "%Y-%m-%d"
            ).date()  # Change to your desired date
            fake_logs_for_day(
                fake_date, min_interval_seconds=10, max_interval_seconds=600
            )  # Random interval: 10s to 10min
        elif int(a) == 4:
            nom = input("Nom del parking: ")
            longitude = input("Longitude: ")
            latitude = input("Latitude: ")
            accesible = input("Accesible? [True/False]: ")

            create_parking_and_planta(
                nom, int(longitude), int(latitude), bool(accesible)
            )
        elif int(a) == 9:
            break
