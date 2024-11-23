# Documentación para la API

- `GET /api/parking`: Devuelve todos los parkings.
- `GET /api/parking/<id-parking>`: Devuelve un parking.
- `GET /api/parking/<id-parking>/plazas`: Devuelve todas las plazas de un parking.
- `GET /api/parking/<id-parking>/plantas`: Devuelve todas las plantas de un parking.
- `GET /api/planta`: Devuelve todas las plantas.
- `GET /api/plaza`: Devuelve todas las plazas
- `GET /api/plazalog`: Devuelve todos los plaza logs.

- `POST /api/parking`: Crea un parking.
- `POST /api/planta`: Crea una planta.
- `POST /api/plaza`: Crea una plaza.
- `POST /api/plazalog` : Crea un plaza log.

## Como buildear el backend?

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install django djangorestframework`
- `cd app`