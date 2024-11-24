import streamlit as st
import requests as rq
from PIL import Image, ImageDraw
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Your App Title",
    page_icon="logo.png",  # Emoji or small image path
    layout="wide",
)

st.sidebar.image("logo.png", use_container_width=True)

if "id_parking" not in st.session_state:
    st.session_state.id_parking = 5

id = st.session_state.id_parking


url1 = f"http://127.0.0.1:8000/api/parking/{id}"
url2 = f"http://127.0.0.1:8000/api/parking/{id}/plantas"


def fetch_data1(url):
    response = rq.get(url)
    response.raise_for_status()
    data = response.json()
    return data


# Define the colors of the rectangles with transparency
rectangle_red = (255, 0, 0, 128)  # Red with 50% transparency (128 out of 255)
rectangle_green = (0, 255, 0, 128)  # Green with 50% tranparency

# Define all the rectangles of the parking places
rectangle_positions1 = [(0 + i * 100, 0, 100 + i * 100, 120) for i in range(5)]  #
rectangle_positions2 = [(0 + i * 100, 180, 100 + i * 100, 300) for i in range(5)]
rectangle_positions = (
    rectangle_positions1 + rectangle_positions2
)  # join all the positions

# st_autorefresh = st.experimental_autorefresh(interval=5000)
st_autorefresh(interval=5000)

# response = rq.get(url1)

# st_autorefresh = st.rerun() if st.rerun() else st.experimental_autorefresh(interval=5000) #refresh data every 5s

response = rq.get(url1)

response2 = rq.get(url2)

data_parking = response.json()  # plazas ocupadas / fetch_data1()

name_parking = data_parking["nom"]  # nombre del parking que se muestra


st.title(f"Distribució del Pàrquing: {name_parking}")


data_plantas = response2.json()  # fetch_data2() #
num_plantas = 0
for item in data_plantas:
    num_plantas += 1

# st.write(num_plantas)

# ocuppied = [item["ocupada"] for item in data]

tab_labels = [item["nom"] for item in data_plantas]
id_plantas = [item["id"] for item in data_plantas]

tabs = st.tabs(tab_labels)

for i, tab in enumerate(tabs):
    with tab:
        url3 = f"http://127.0.0.1:8000/api/planta/{id_plantas[i]}/plazas"
        response3 = rq.get(url3)
        data_plazas = response3.json()
        ocuppied = [item["ocupada"] for item in data_plazas]

        st.subheader(f"Distribució pàrquing")

        image_url = "../docs/parking-layout.png"

        # st.image(image_url)

        base_image = Image.open(image_url).convert(
            "RGBA"
        )  # Ensure image is in RGBA mode for transparency

        if data_parking["accesible"]:
            disabled_url = "../docs/disabled.png"
            disabled_image = Image.open(disabled_url).convert("RGBA")
            disabled_image = disabled_image.resize((70, 50))
            position = (15, 35)

            base_image.paste(disabled_image, position, disabled_image)

        # Create an overlay image the same size as the base image
        overlay = Image.new(
            "RGBA", base_image.size, (0, 0, 0, 0)
        )  # Transparent overlay
        draw = ImageDraw.Draw(overlay)

        # n =len(rectangle_positions)
        for i in range(min(10, len(ocuppied), len(rectangle_positions))):
            # Draw the transparent rectangle on the overlay
            if ocuppied[i]:
                draw.rectangle(rectangle_positions[i], fill=rectangle_red)
            else:
                draw.rectangle(rectangle_positions[i], fill=rectangle_green)

        # Combine the base image with the overlay
        combined_image = Image.alpha_composite(base_image, overlay)

        # Display the result in Streamlit
        st.image(combined_image, use_container_width=True)


# st.write(ocuppied)

# st.write(data)

