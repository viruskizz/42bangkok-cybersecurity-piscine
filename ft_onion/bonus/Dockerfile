FROM node:bookworm
LABEL authors="viruskizz"

## Prerequisite
RUN apt-get update -y && apt-get install -y \
    basez \
    vim \
    openssh-server \
    tor
COPY conf/torrc             /etc/tor/
COPY conf/sshd_default.conf /etc/ssh/sshd_config.d/
COPY tools                  /tools

## Prepare user and create ssh-keygen
RUN useradd ${USER} \
    -g users \
    -m \
    -p $(openssl passwd -6 "${PASS}")
USER viruskizz
RUN /tools/generate-ssh.sh

## Setup application
WORKDIR /app
COPY app/package.json .
RUN npm install
COPY app .

## To run docker entrypoint
USER root
ENTRYPOINT [ "/tools/docker-entrypoint.sh" ]
