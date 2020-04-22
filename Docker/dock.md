
# Docker : 


## Définition :
<p> A définir </p>

 <img src="https://docs.docker.com/engine/images/engine-components-flow.png">

  <img src="https://docs.docker.com/engine/images/architecture.svg">


## Sources :
<p>https://docs.docker.com/get-started/overview/</p>
<p>https://www.ionos.fr/digitalguide/serveur/configuration/tutoriel-docker-installation-et-premiers-pas/</p>


## Exo :
* ### __A quoi sert un Dockerfile :__
<p>Un dockerfile est un fichier text qui contient toutes les commandes pour assembler une image docker. A l’aide de la commande docker build l’utilisateur peut créer un buid automatique a l’aide des instructions mises dans le fichier.</p>

* ###  __lancer votre premier container docker :__

<p> travailler avec docker : </p>

```bash
sudo systemctl enable docker
sudo systemctl disable docker

sudo systemctl status docker

sudo systemctl start docker
sudo systemctl stop docker
sudo systemctl restart docker
```
<p> Hello world: </p>

```bash
sudo docker run hello-world 
```

<p> Pour executer un container ubuntu:</p>

```bash
sudo docker run [OPTIONS] IMAGE [:TAG|@DIGEST] [CMD] [ARG...]

sudo docker run ubuntu 
sudo docker run -it ubuntu bash
```


* ### __regarder si votre container est bien lancer :__

<p>Voir les containers actifs:</p>

```bash
docker ps [OPTIONS]

docker ps
```

<p>Voir les containers existant:</p>

```bash
docker container ls
```


* ### __vérifier en vous connectant à votre container qu'il est bien up et qu'il s'aggit bien de lui:__


<p>Voir les containers actifs et vérifier le container ID:</p>

```bash
docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
b9c1ed6fd170        ubuntu              "bash"              3 seconds ago       Up 2 seconds                            compassionate_brattain
```

<p>Sur le container taper la commande hostname pour vérifier si l'hostname du container correspond bien à l'ID</p>

```bash
hostname
b9c1ed6fd170

#ou

echo $HOSTNAME
b9c1ed6fd170

```

<p>Afficher l'ID au complet</p>

```bash
docker ps -a --no-trunc -q
```

# CHEAT SHEET

## Build
__Build an image from the Dockerﬁle in the current directory and tag the image:__
```bash
docker build -t myimage:1.0 .
```
__List all images that are locally stored with the Docker Engine:__
```bash
docker image ls
```
__Delete an image from the local image store:__

```bash
docker image rm alpine:3.4
```
## Run
__Run a container from the Alpine version 3.9 image, name the running container__
__“web” and expose port 5000 externally, mapped to port 80 inside the container:__
```bash
docker container run --name web -p 5000:80 alpine:3.9
```
__Stop a running container through SIGTERM:__
```bash
docker container stop web
```
__Stop a running container through SIGKILL:__
```bash
docker container kill web
```
__List the networks:__
```bash
docker network ls
```
## Share
__Pull an image from a registry:__
```bash
docker pull myimage:1.0
```
__Retag a local image with a new image name and tag:__
```bash
docker tag myimage:1.0 myrepo/ myimage:2.0
```
__Push an image to a registry:__
```bash
docker push myrepo/myimage:2.0
```
__List the running containers (add --all to include stopped containers):__
```bash
docker container ls
```
__Delete all running and stopped containers:__
```bash
docker container rm -f $(docker ps -aq)
```
__Print the last 100__
__lines of a container’s logs:__

```bash
docker container logs --tail 100 web
```





