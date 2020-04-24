## Etapes :
__Après avoir configuré le Dockerfiles__

<p> Dans le repertoir du Dockerfile: </p>

```bash
docker build -t NAME .

docker run -p 8000:8888  NAME
```

<p>  le container va s'éxecuter avec jupyter </p>
<P> la commande suivante permet d'ajouter l'utilisateur courant au groupe Docker pour l'exploiter sans les droits administrateurs </p>

```bash 
sudo groupadd docker
sudo gpasswd -a $USER docker
```
