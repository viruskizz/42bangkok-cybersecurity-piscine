NAME=vaccine

$(NAME): all

all: up

dev:
	docker compose up --build

up:
	docker compose up --detach --build

exec:
	docker exec -it ${NAME}-app /bin/bash

stop:
	docker compose stop

down:
	docker compose down

re: down up

clean: down
	-docker rmi -f $$(docker images "${NAME}-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

fclean: clean
	-rm -rf output

.PHONY: up down stop clean fclean re exec