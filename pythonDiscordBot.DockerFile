FROM ubuntu:20.04

ARG version=1.0.0-SNAPSHOT

COPY ./PythonDiscordBot /home/PythonDiscordBot

EXPOSE 80
EXPOSE 443

RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get install -y python3.5
RUN apt-get install -y python3-pip
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y tzdata
RUN apt -y update
RUN apt -y install libffi-dev libnacl-dev python3-dev
RUN apt -y install ffmpeg

RUN yes | pip3 install discord.py==1.7.3
RUN yes | pip3 install youtube_dl==2021.6.6
RUN yes | pip3 install pycoingecko==2.2.0
RUN yes | pip3 install PyNaCl==1.4.0
WORKDIR /home/PythonDiscordBot


CMD  python3 main.py