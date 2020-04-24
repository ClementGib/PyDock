# API :
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

## FLASK

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

### Mise en place du serveur :

<p>Hello world:</p>

<img src="https://github.com/ClementGib/PyDock/blob/master/Images/flask.png">
<img src="https://github.com/ClementGib/PyDock/blob/master/Images/server.png">


__Fichiers__

<p>main.py :</p>
```Python
from app import app
```

<p>__init__.py de app :</p>
```Python
from flask import Flask
app = Flask(__name__)
from app import views
from app import books
```

<p>Books.py :</p>
```Python
from app import app                                                                    
from flask import send_file
@app.route('/books')
def download():
    try:
        path = "books.json"
        return send_file(path, as_attachment=True)
    except Exception as e:
        return str(e)
```

<img src="https://github.com/ClementGib/PyDock/blob/master/Images/temp.PNG">

__Arborescence du serveur :__
<p></p>
<img src="https://github.com/ClementGib/PyDock/blob/master/Images/Arbo">




### Automatisation :

__scripts__
<p>start.sh :</p>
```bash
#!/bin/bash

#creation du container
app="docker.server"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app
```

<p>remove.sh :</p>

```bash
#!/bin/bash

#détruit le container
ID=$(docker ps -aqf "name=docker.server")
docker kill $ID 
docker rm $ID
```

<p>test_api.sh :</p>

```bash
#!/bin/bash
COMMAND=$(docker ps |  grep docker.server)

#Verification du container 
if [ -z "$COMMAND" ]; then
  app="docker.server"
  docker build -t ${app} .
  docker run -d -p 56733:80 \
    --name=${app} \
    -v $PWD:/app ${app}
      
  docker ps
  else
      echo $COMMAND
fi
#laisser le temps de démarrer
sleep 2
GET 192.168.1.18:56733 
```

<p></p>
<img src="https://github.com/ClementGib/PyDock/blob/master/Images/GET.PNG">
