#!/bin/bash

#creation du container
app="docker.server"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app}

docker ps
