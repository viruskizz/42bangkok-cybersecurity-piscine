FROM python:3.13.2-bookworm

ARG USER=infection
ARG PASS=infection

RUN apt-get update -y && apt-get -y install \
    sudo \
    vim

RUN useradd ${USER} \
    -g users \
    -G sudo \
    -m \
    -p $(openssl passwd -6 "${PASS}")

RUN mkdir -p /users/src/app && \
    chown -R ${USER}:users /users/src/app

COPY --chown=${USER}:users backup/ /home/infection/

## Configuration python app

WORKDIR /usrs/src/app

COPY app .

RUN pip install -r requirements.txt

CMD ["sleep", "infinity"]