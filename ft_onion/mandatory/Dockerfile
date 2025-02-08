FROM nginx:bookworm
LABEL authors="viruskizz"

ARG USER=viruskizz
ARG PASS=viruskizz

RUN apt-get update -y

RUN apt-get install -y \
    sudo \
    vim \
    openssh-server \
    tor

RUN mkdir /var/run/sshd

COPY conf/default.conf      /etc/nginx/conf.d/
COPY conf/nginx.conf        /etc/nginx/
COPY conf/torrc             /etc/tor/
COPY conf/sshd_default.conf /etc/ssh/sshd_config.d/
COPY tools                  /tools

COPY index.html /usr/share/nginx/html

RUN useradd ${USER} \
    -g users \
    -G sudo \
    -m \
    -p $(openssl passwd -6 "${PASS}")

ENTRYPOINT [ "/tools/docker-entrypoint.sh" ]