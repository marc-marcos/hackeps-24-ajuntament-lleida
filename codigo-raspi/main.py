import requests

ADDRESS = "http://127.0.0.1:8000/"

# Get all the parkings
parkings = requests.get(f"{ADDRESS}api/parking/").json()

for parking in parkings:
    print(parking)

id_p = input("Enter the id of the parking you want to change: ")

# Get all the floors of that parking

floors = requests.get(f"{ADDRESS}api/parking/{id_p}/plantas/").json()

for floor in floors:
    print(floor)

id_f = input("Enter the id of the floor you want to change: ")

# Get all the spots of that floor

spots = requests.get(f"{ADDRESS}api/parking/{id_p}/plazas/").json()

for spot in spots:
    print(spot)

id_plaza = input("Enter the id of the spot you want to select: ")

# Change the state of that floor

while True:
    data = {"ocupada": True, "planta": id_p}

    headers = {"Content-Type": "application/json"}

    response = requests.put(
        f"{ADDRESS}api/plaza/{id_plaza}/", json=data, headers=headers
    )

    print(response.status_code)

    wait_input = input()

    data = {"ocupada": False, "planta": id_p}

    headers = {"Content-Type": "application/json"}

    response = requests.put(
        f"{ADDRESS}api/plaza/{id_plaza}/", json=data, headers=headers
    )

    print(response.status_code)

    wait_input = input()
