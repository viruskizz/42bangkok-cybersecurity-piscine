
NAME=ft_onion

$(NAME): all

all: up

up:
	docker compose up -d

dev:
	docker compose up -d --buil

stop:
	docker compose stop

down:
	docker compose down

re: down up

clean: down
	-docker rmi -f $$(docker images "${NAME}*" | awk 'NR!=1 {print}' | awk '{print $$1}')

.PHONY: mkdir_data up down stop clean fclean re