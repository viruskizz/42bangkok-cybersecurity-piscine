FROM node:bookworm

RUN apt-get update -y && apt-get install -y \
    tor \
    vim

COPY conf/torrc /etc/tor/
COPY tools      /tools

WORKDIR /app

COPY app/package.json .

RUN npm install

COPY app .

ENTRYPOINT [ "/tools/docker-entrypoint.sh" ]