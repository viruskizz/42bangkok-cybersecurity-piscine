FROM python:3.13.2-bookworm

ARG USER=viruskizz
ARG PASS=viruskizz

RUN apt-get update -y && apt-get -y install \
    sudo \
    vim

RUN useradd ${USER} \
    -g users \
    -G sudo \
    -m \
    -p $(openssl passwd -6 "${PASS}")

RUN mkdir -p /users/src/app && \
    chown -R viruskizz:users /users/src/app

USER viruskizz

RUN mkdir /home/infection && \
    chmod 777 /home/infection


## Configuration python app

WORKDIR /usrs/src/app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app .

CMD ["sleep", "infinity"]