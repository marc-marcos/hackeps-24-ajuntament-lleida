# hackeps-24-ajuntament-lleida

## Què és AparcaXmi
**AparcaXmi** permet als usuaris trobar places lliures de pàrquing entre els diversos pàrquings ubicats al mapa.

Cada punt al mapa representa una ubicació d'un pàrquing, si està en vermell vol dir que no té cap plaça lliure i verd, en cas contrari. Tot això é spossiible gràcies a un sensor programat en una RaspberryPi. En seleccionar un pàrquing es pot visualitzar informació rellevant sobre el pàrquing, incloent el nom del pàrquing, nombre de places lliures i si té places per a discapacitats. Si, s'ha seleccionat un pàrquing, en una altra pestanya es pot visualitzar la distribució de les places llliures d'aquell pàrquing seleccionat per plantes que estan pintades de verd i vermelles si estan ocupades; addicionalment té un símbol de discapacitat si està reservat per a ells, per tal de que ràpidament es pugui observar la disponibilitat.

## Documentació 
__Els fitxers que s'esmenten en aquest readme es troben en la carpeta base de hackeps...__

Abans de possar-nos a programar, hem volgut organitzar-nos bè. Hem dissenyat tant a nivell back com a nivell front dissenys del que ha acabat sent la nostra propera pàgina.

Pel que fa al backend, s'ha fet un UML amb mermaid per organitzar la base de dades i garantir claretat i portabilitat.

En el frontend, hem fet a mà un disseny de l'interficie web i hem organitzat les diverses pestanyes.

Tot això està organitzat en una carpeta nombrada docs.

Tambè per facilitar la instal·lació a qualsevol ordinador, hem creat un requeriments.txt que es pot executar per que t'instal·li directament les llibreries que hem fet servir.

```
pip install -r backend/app/requirements.txt
pip intsall -r frontend-web/requirements.txt
```

Tambè hi ha a part un DOCS.md en el backend on explica el funcionament de com fer peticions entre altrees coses a la base de dades i com fer servir l'environmengt de python. Existeix una altra carpeta nombrada utils on hi ha un script per automatitzar la pujada de dades a la database.

## Workflow
Hem treballat en branques per garantir la modularitat, el paral·lelisme, reducció d'errors entre conflictes, capacitat de fer rollback, eficiència... A més a més, hem posat noms als commits per millorar la legibilitat.

A l'hora de prendre decicions ens informàvem tant al front com al back per garantir que les dues parts es complementaben bè.

Cada vegada que hi havia un error, es debuguejava i es feia un commit actualitzant-ho. Fins que no funcionava bé al testejar-ho, no es feia commit.

Hem tingut cura a l'hora de nombrar les nostres variables per tenir un codi clar i lògic.

## Saber-ne més
[Ves al devpost](https://devpost.com/software/aparcaxmi?ref_content=user-portfolio&ref_feature=in_progress)
