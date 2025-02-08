FROM node:bookworm
LABEL authors="viruskizz"

ARG USER=viruskizz
ARG PASS=viruskizz

RUN apt-get update -y && apt-get install -y \
    basez \
    sudo \
    vim \
    openssh-server \
    tor

COPY conf/torrc             /etc/tor/
COPY conf/sshd_default.conf /etc/ssh/sshd_config.d/
COPY tools                  /tools

RUN useradd ${USER} \
    -g users \
    -G sudo \
    -m \
    -p $(openssl passwd -6 "${PASS}")

WORKDIR /app

COPY app/package.json .

RUN npm install

COPY app .

ENTRYPOINT [ "/tools/docker-entrypoint.sh" ]