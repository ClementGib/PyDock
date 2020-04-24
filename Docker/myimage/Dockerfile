#Download base image ubuntu
#FROM ubuntu:18.04
FROM ubuntu:latest



#Dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y build-essential vim  python3 python3-pip python3-dev

WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace

RUN pip3 freeze > requirements.txt \
    pip3 install -r requirements.txt && \
    pip3 install jupyter

#Expose port 8888
EXPOSE 8000

CMD ["sh", "-c" , "jupyter notebook --no-browser --port=8000 --ip='0.0.0.0' --allow-root"]
