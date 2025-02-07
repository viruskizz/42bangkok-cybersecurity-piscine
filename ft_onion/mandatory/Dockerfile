FROM nginx:bookworm

RUN apt-get update -y

RUN apt-get install -y \
    systemd \
    tor \
    vim \
    procps

COPY conf/default.conf  /etc/nginx/conf.d/
COPY conf/nginx.conf    /etc/nginx/
COPY conf/torrc         /etc/tor/
COPY index.html         /usr/share/nginx/html

COPY tools /tools

ENTRYPOINT [ "/tools/docker-entrypoint.sh" ]