#Download base image ubuntu
FROM ubuntu:18.04

#Dependencies
RUN apt-get update && apt-get install -y vim  python3 python3-pip

WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace

RUN pip3 freeze > requirements.txt \
    pip3 install -r requirements.txt && \
    pip3 install jupyter

#Expose port 8888
EXPOSE 8888

CMD ["sh", "-c" , "jupyter notebook --no-browser --port=8000 --ip='0.0.0.0' --allow-root"]
