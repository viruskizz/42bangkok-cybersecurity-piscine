NAME=inquisitor

$(NAME): all

all: up

up:
	docker compose up --detach --build

exec-server:
	docker exec -it server /bin/bash

exec-src:
	docker exec -it src /bin/bash

exec-dest:
	docker exec -it dest /bin/sh

network:
	docker network inspect inquisitor_main | jq '.[].Containers[] | {name: .Name, mac: .MacAddress, ip: .IPv4Address}'

stop:
	docker compose stop

down:
	docker compose down

re: down up

clean: down
	-docker rmi -f $$(docker images "${NAME}-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

.PHONY: up exec down stop clean fclean re
