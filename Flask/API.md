## API :
__Application Programmable Interface__


<img src="https://camo.githubusercontent.com/a364f9aa763e0b5dba55b0bb0348f65a24357b89/68747470733a2f2f692e7974696d672e636f6d2f76692f5551776a7974517a6f71452f6d617872657364656661756c742e6a7067">

<p> Les requètes HTTP </p>

* GET effectue une lecture
* POST crée une donnée
* PUT met à jour une donnée
* DELETE supprime une donnée

<p> Code de retour HTTP </p>

* 200 : Succès
* 400 : Erreur de syntaxe
* 404 : Introuvable
* 403 : Interdit
* 500 : Erreur interne à l'API, il est préférable de gérer cette erreur en interne pour retourner le code adéquoit.


<p> Une API est généralement un service temps réel prévu pour être exploité par d'autre logiciel </p>


__Flask est un micro web Framework fait et pour Python__

```bash
https://hub.docker.com/r/jcdemo/flaskapp
```

__Flask Dockerfile__

```bash
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
```

<p> Définition du répertoire flask TestApp et script d'installation :</p>

__start.sh__
```bash
#!/bin/bash

#creation du container
app="docker.server"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app
```

__remove.sh__
```bash
#!/bin/bash

#détruit le container
ID=$(docker ps -aqf "name=docker.server")
docker kill $ID 
docker rm $ID
```

__Arborescence du serveur :__
<img src="PyDock/Images/Arbo.png">
