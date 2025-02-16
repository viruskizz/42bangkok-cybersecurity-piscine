FROM python:3-bookworm

RUN apt-get update -y && apt-get install -y \
    iputils-ping \
    net-tools \
    vim


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "tail", "-f",  "/dev/null" ]