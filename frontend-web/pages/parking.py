import streamlit as st
import requests as rq

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
            
            #image_url = "pages/images/parking_scheme.svg"

            #st.image(image_url, use_column_width=True)

            for ocup in ocuppied:
                    if ocup:
                            st.write("ocupat")
                    else:
                            st.write("no ocupat")


                        

#st.write(ocuppied)

#st.write(data)