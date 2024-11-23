import streamlit as st
import requests as rq

st.title("Distribució del Pàrquing")

if 'id_parking' not in st.session_state:
        st.session_state.id_parking = 1

id = st.session_state.id_parking

url1 = f'http://127.0.0.1:8000/api/parking/{id}/plazas'
url2 = f'http://127.0.0.1:8000/api/parking/{id}/plantas'

response = rq.get(url1)

response2 = rq.get(url2)

data = response.json() #plazas ocupadas


data_plantas = response2.json()
num_plantas = 0
for item in data_plantas:
        num_plantas += 1

#st.write(num_plantas)

ocuppied = [item["ocupada"] for item in data]

tab_labels = [item["nom"] for item in data_plantas]
tabs = st.tabs(tab_labels)

for i, tab in enumerate(tabs):
        with tab:
            st.subheader(f"Distribució pàrquing ")
            for ocup in ocuppied:
                    if ocup:
                            st.write("ocupat")
                    else:
                            st.write("no ocupat")


                        

#st.write(ocuppied)

#st.write(data)