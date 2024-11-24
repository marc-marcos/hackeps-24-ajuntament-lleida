# Get a dataframe of the
from collections import defaultdict
import pandas as pd
from datetime import datetime
import requests


def get_raw_data():
    request = requests.get("http://127.0.0.1:8000/api/plazalog")

    d = request.json()

    df = pd.DataFrame(d)

    print(df)

    return df


def get_last_data():
    request = requests.get("http://127.0.0.1:8000/api/plazalog")

    d = request.json()

    counts = defaultdict(lambda: {"is_entrada": 0, "not_is_entrada": 0})

    processed_data = []
    for entry in d:
        # Parse the hour from datahora
        hour = datetime.fromisoformat(entry["datahora"]).strftime("%Y-%m-%d %H:00")
        processed_data.append({"hour": hour, "is_entrada": entry["is_entrada"]})

    # Convert to pandas DataFrame
    df = pd.DataFrame(processed_data)

    # Step 2: Group by hour and count entries and exits
    result = df.groupby("hour")["is_entrada"].value_counts().unstack(fill_value=0)
    result.rename(columns={True: "Entries", False: "Exits"}, inplace=True)

    # Reset the index for easier plotting
    result.reset_index(inplace=True)

    # Display the DataFrame
    return result


# Get the last status of the parking and backtrack the initial state


def get_accumulated_vehicles():
    req1 = requests.get("http://127.0.0.1:8000/api/parkingstatus")
    req2 = requests.get("http://127.0.0.1:8000/api/plazalog")

    parking_status = req1.json()
    plaza_log = pd.DataFrame(req2.json())

    # Initialize the 'cars_in_garage' column
    plaza_log["cars_in_garage"] = 0

    # Start with the final number of cars from parking_status["occupied_spots"]
    plaza_log.loc[plaza_log.index[0], "cars_in_garage"] = parking_status[
        "occupied_spots"
    ]

    for i in range(1, len(plaza_log)):
        if plaza_log.iloc[i - 1][
            "is_entrada"
        ]:  # If previous row was an entry, subtract 1
            plaza_log.loc[plaza_log.index[i], "cars_in_garage"] = (
                plaza_log.loc[plaza_log.index[i - 1], "cars_in_garage"] - 1
            )
        else:  # If previous row was an exit, add 1
            plaza_log.loc[plaza_log.index[i], "cars_in_garage"] = (
                plaza_log.loc[plaza_log.index[i - 1], "cars_in_garage"] + 1
            )

    # Sort the DataFrame by 'DateTime'
    plaza_log.sort_values("datahora", inplace=True)

    return plaza_log
