import streamlit as st
import requests as rq
from PIL import Image, ImageDraw

# Define rectangle position, size, and color (with transparency)
rectangle_positions = (0, 0, 100, 120) # (left, top, right, bottom)
rectangle_red = (255, 0, 0, 128)  # Red with 50% transparency (128 out of 255)
rectangle_green = (0, 255, 0, 128) # Green with 50% tranparency


st.title("Distribució del Pàrquing")

if 'id_parking' not in st.session_state:
        st.session_state.id_parking = 1

id = st.session_state.id_parking
id_planta = 1
#url1 = f'http://127.0.0.1:8000/api/parking/{id}/plazas'
url2 = f'http://127.0.0.1:8000/api/parking/{id}/plantas'

#response = rq.get(url1)

response2 = rq.get(url2)

#data = response.json() #plazas ocupadas


data_plantas = response2.json()
num_plantas = 0
for item in data_plantas:
        num_plantas += 1

#st.write(num_plantas)

#ocuppied = [item["ocupada"] for item in data]

tab_labels = [item["nom"] for item in data_plantas]
id_plantas = [item["id"] for item in data_plantas]

tabs = st.tabs(tab_labels)

for i, tab in enumerate(tabs):
        with tab:
            url3 = f'http://127.0.0.1:8000/api/planta/{id_plantas[i]}/plazas'
            response3 = rq.get(url3)
            data_plazas = response3.json()
            ocuppied = [item["ocupada"] for item in data_plazas]

            st.subheader(f"Distribució pàrquing")
            
            image_url = "../docs/parking-layout.png"

            #st.image(image_url)

            base_image = Image.open(image_url).convert("RGBA")  # Ensure image is in RGBA mode for transparency

            # Create an overlay image the same size as the base image
            overlay = Image.new("RGBA", base_image.size, (0, 0, 0, 0))  # Transparent overlay
            draw = ImageDraw.Draw(overlay)

            n =len(rectangle_positions)
            for i in range(1):
            # Draw the transparent rectangle on the overlay
                if ocuppied[i]:
                    draw.rectangle(rectangle_positions, fill=rectangle_red)
                else:
                    draw.rectangle(rectangle_positions, fill=rectangle_green)  

            # Combine the base image with the overlay
            combined_image = Image.alpha_composite(base_image, overlay)

            # Display the result in Streamlit
            st.image(combined_image, use_container_width=True)




                        

#st.write(ocuppied)

#st.write(data)