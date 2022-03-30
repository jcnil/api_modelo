# REST API - Python - Flask

REST API creada con Python, el framework web Flask y con data que se descargo en un archivo JSON se las ciudades de Estados Unidos de America y Canada, con el protocolo HTTP y el método GET.

<hr/>


## Para Correger la aplicacion se debe:

1. Crear un virtualenv en mi caso use pyenv para crear un entorno virtual:

    `$ pyenv virtualenv 3.9.5  <nombre_ambiente>`

    Luego se activa el entorno virtual:

    `$ pyenv activate <nombre_ambiente>`

    y posteriormente se corre el paso 2, para mayor insformacion consultar la pagina https://realpython.com/intro-to-pyenv/     

2. Instalar las librerias que estan en el archivo de requirements.txt ejecuntado el siguiente comando

   `$ pip3 install -r requirements.txt`

3. Luego a traves del shell se ingresa a la carpeta principal, luego ingresas a la carpeta controlles y se ejecuta el siguiente comando

   `$ flask run`

Ahora, la API está escuchando en el puerto localhost 5000. Los endpoints son:

 - [http://127.0.0.1:5000/search?q=Londo&latitude=43.70011&longitude=-79.4163](http://127.0.0.1:5000/search?q=Londo&latitude=43.70011&longitude=-79.4163)
 - [http://127.0.0.1:5000/suggestions?q=SomeRandomCityInTheMiddleOfNowhere](http://127.0.0.1:5000/suggestions?q=SomeRandomCityInTheMiddleOfNowhere)

 ### Estructura del código

El árbol de directorios del código fuente se ve así:

```
.
├── application
│   ├── __init__.py
│   └── services
│       ├── searchs.py
│       ├── suggestions.py
│       └── __init__.py
├── controller
│   ├── app.py ---------------> API entry point
│   ├── __init__.py
├── infrastructure
│   └── data
│       ├── CA_final.json
│       └── US_final.json
├── requirements.txt
└── test
    ├── application
    │   ├── __init__.py
    │   └── test_services.py
    ├── base_test_case.py
    ├── controller
    │   ├── __init__.py
    │   └── test_app.py
    └── __init__.py
```

## Pruebas


### Ejecutando pruebas

Las pruebas se han creado con [Unittest](https://docs.python.org/3/library/unittest.html).

## Solucion por

* José Nicolielly - - [jcnil](https://github.com/jcnil/api_modelo)
