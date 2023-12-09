### 
#Base Image
###
FROM ubuntu:22.04

##Labels
LABEL version="0.1"
LABEL description="Custom image to allow to train models with pytorch"
RUN apt-get update && apt-get install -y \
    python3-pip 
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt 

COPY \. /app
EXPOSE 50055 

WORKDIR /app
ENTRYPOINT ["/boot.sh"]