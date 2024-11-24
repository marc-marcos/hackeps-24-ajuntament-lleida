import streamlit as st
from graphics_library import get_last_data, get_accumulated_vehicles, get_raw_data
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="Your App Title",
    page_icon="logo.png",  # Emoji or small image path
    layout="wide",
)

st.sidebar.image("logo.png", use_container_width=True)

d = get_last_data()

st.header("Graphics and Statistics")

st.write("Hourly entries and exits in the parking garage")

st.bar_chart(
    d,
    x="hour",
    y=["Exits", "Entries"],
    color=["#FF0000", "#0000FF"],  # Optional
)

d2 = get_accumulated_vehicles()

line_chart = (
    alt.Chart(d2)
    .mark_line()
    .encode(x="datahora", y="cars_in_garage", tooltip=["datahora", "cars_in_garage"])
    .properties(title="Number of Cars in Garage Over Time", width=700, height=400)
)

st.altair_chart(line_chart, use_container_width=True)

d = get_raw_data()

df = pd.DataFrame(d)

# Convert `datahora` to datetime for sorting
df["datahora"] = pd.to_datetime(df["datahora"])

# Sort the DataFrame by `datahora`
df.sort_values("datahora", inplace=True)

# Create an `end_time` column for the bar segments (use the next event's `datahora` as the end time)
df["end_time"] = df["datahora"].shift(-1)
df["end_time"].iloc[-1] = df["datahora"].iloc[-1] + pd.Timedelta(
    minutes=5
)  # Add a small buffer for the last event

# Create a horizontal bar chart
solid_bar_chart = (
    alt.Chart(df)
    .mark_bar(height=150)  # Single horizontal bar
    .encode(
        x=alt.X("datahora:T", title="Time"),
        x2=alt.X2("end_time:T"),  # Define segment endpoints
        y=alt.value(0),  # Fix the y-position for a single bar
        color=alt.Color(
            "is_entrada:N",
            title="Type",
            scale=alt.Scale(
                domain=[True, False],
                range=["green", "red"],  # Green for entries, red for exits
            ),
        ),
        tooltip=["datahora", "end_time", "is_entrada"],
    )
    .properties(
        title="Garage Activity Timeline",
        width=800,
        height=300,
    )
)

# Display the chart in Streamlit
st.altair_chart(solid_bar_chart, use_container_width=True)
