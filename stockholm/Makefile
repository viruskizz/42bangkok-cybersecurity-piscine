NAME=stockholm

$(NAME): all

all: up

up:
	docker compose up --detach --build

exec:
	docker exec -it stockholm /bin/bash

stop:
	docker compose stop

down:
	docker compose down

cp:
	docker cp backup/. stockholm:/home/infection/

clean: down
	-rm -rf app/__pycache__
	-rm -rf $$(find . -name '*.rv' -o -name '*.ft' -o -name '*.pem' -o -name '*.key')
	-rm -rf infection
	-docker rmi -f $$(docker images "stockholm-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

.PHONY: mkdir_data up down stop clean fclean re
