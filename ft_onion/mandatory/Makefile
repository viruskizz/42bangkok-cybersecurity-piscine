
NAME=ft_onion

$(NAME): all

all: up

exec:
	docker exec -it onion /bin/bash

up:
	docker compose up

dev:
	docker compose up --build

stop:
	docker compose stop

down:
	docker compose down

re: down up

clean: down
	-docker rmi -f $$(docker images "mandatory-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

.PHONY: mkdir_data up down stop clean fclean re