
NAME=ft_onion

$(NAME): all

all: up

up:
	docker compose up -d

dev:
	docker compose up --build
	docker cp onion_bonus:/tmp/auth ./auth
	docker cp onion_bonus:/tmp/ssh ./ssh

exec:
	docker exec -it onion_bonus /bin/bash

stop:
	docker compose stop

down:
	docker compose down

re: down up

clean: down
	-rm -rf auth
	-rm -rf ssh
	-docker rmi -f $$(docker images "bonus-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

.PHONY: mkdir_data up down stop clean fclean re