NAME=inquisitor

$(NAME): all

all: up

up:
	docker compose up --detach --build

exec-server:
	docker exec -it ${NAME}-server-1 /bin/bash

exec-client:
	docker exec -it ${NAME}-client-1 /bin/bash

stop:
	docker compose stop

down:
	docker compose down

clean: down
	-docker rmi -f $$(docker images "${NAME}-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

.PHONY: up exec down stop clean fclean re
