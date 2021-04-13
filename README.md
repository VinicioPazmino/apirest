# DevOps Technical Assessment

[![Build Status](https://dev.azure.com/vinidavid17/Pichincha-DevOps/_apis/build/status/apirest?branchName=master)](https://dev.azure.com/vinidavid17/Pichincha-DevOps/_build/latest?definitionId=3&branchName=master)

# Introduction 
Este repositorio crea un microservicio de API REST en lenguaje de programacion de python con framework FLASK 

## Getting Started
Instrucciones para ejecutar en sistema lcoal:
1.	Posicionarse en el directorio **/apirest/dev
2.	Ejecutar:
```
pip install -r requierements.txt 
python app.py
```
3. Dirigirse al navegador como "loclahost/5000/DevoOps"

## Buiild imagen Docker and Create the container (Local) 
1. Posicionarce en el directorio donde se encuentre el Dockerfile

```
docker build -t apirest .       // Construir magen <apirest> carpeta donde esta los archivos dockerfile
docker run -it -p 5000:5000 -d apirest      // ejecutar docker y dejar libre consola
docker ps                                   // visualizar contenedores que se estan ejecutando 
docker stop <ID>
```

## Directories
Este repositorio contiene codigo para desarrollo (dev) de la aplicacion en python, Directorios: 
- README.md
- azure-pipelines.yml
- dev
    - app.py
    - Dockerfile
    - requirements.txt

## CI/CD
1.	Subir repositorio en REPOS de azure
2.	Crear la pipeline con el archivo YAML. 
3.  El pipeline genera las instrucciones para hacer BUILD de la imagen de docker y hacer un PUSH en el ACR (Azure Container Registry), posteriormente publica un Artifact para usarla en una RELEASE
4.	Crear una Release pipeline, la confoguracion de esta release tiene 3 tareas (Borrar un contenedor anterior, Crear un nuevo contenedor, resetear la cache para asegurar la ejecucion del contenedor)
5.	Se genera una ACI (Azure container Instance) 
6. [http://devops.eastus.azurecontainer.io:5000/DevOps](http://devops.eastus.azurecontainer.io:5000/DevOps)
7. con HTTP GET, PUT, PATCH, DELETE el mensage es 'ERROR'
8. con HTTP POST el mensaje es:
```
    [
    {
        "message": "Hello Juan Perez your message will be send"
    },
    {
        "token": "xxxxxx.yyyyyy.zzzzz"
    }
    ]
```

### Repositorio
- [VinicioPazmino/apirest](https://github.com/VinicioPazmino/apirest)