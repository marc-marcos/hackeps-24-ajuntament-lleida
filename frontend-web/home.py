import streamlit as st

st.set_page_config(
    page_title="Your App Title",
    page_icon="logo.png",  # Emoji or small image path
    layout="wide",
)

st.sidebar.image("logo.png", use_container_width=True)

st.title("Home")

if "id_parking" not in st.session_state:
    st.session_state.id_parking = 1

st.header("Vols assegurarte de tenir espai per aparcar al arribar al _parking_?")

st.markdown("### Eines per a usuaris.")

st.markdown(
    "1. Selecciona el parking al que vols aparcar a la pestaña de *Mapa*. Aquí se't indicaran també els parkings amb places lliures i als que no els hi queda ninguna."
)
st.markdown(
    "2. Quan ho tinguis seleccionat, canvia a la pestanya *Parking*, per poder veure en temps real la ocupació de les diverses places del parking."
)

st.markdown("### Eines per a administradors.")

st.markdown(
    "1. Pots accedir a la pestanya de _Graphics_ on pots trobar totes les dades referents a les dades històriques d'ocupació del parking."
)

st.markdown(
    "2. A més, pots accedir a la pestanya de _Manage_, per tal de canviar manualment alguna plaça si no s'ha introduit correctament, o per afegir plantes o parkings nous."
)

st.markdown(
    "3. També tens disponible la pestanya de _Historial_ on trobaràs tots els logs del que ha succeït als teus parkigns."
)
