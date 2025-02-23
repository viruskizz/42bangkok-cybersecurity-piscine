NAME=vaccine
APP_FILE=docker-compose.app.yml
DVWA_FILE=docker-compose.dvwa.yml

$(NAME): all

all: up

up: dvwa app

down: down-dvwa

re: down up

clean: down
	-docker rmi -f $$(docker images "${NAME}-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

fclean: clean fclean-dvwa

.PHONY: up down stop clean fclean re

### DVWA ###
dvwa:
	docker compose -f ${DVWA_FILE} up --detach --build

exec-dvwa:
	docker exec -it ${NAME}-app /bin/bash

stop-dvwa:
	docker compose -f ${DVWA_FILE} stop

down-dvwa:
	docker compose -f ${DVWA_FILE} down

fclean-dvwa:
	sudo rm -rf pgdata mydata
	sudo rm -rf $$(find dvwa/*/migrations ! -name __init__.py -type f)

.PHONY: dvwa exec-dvwa stop-dvwa down-dvwa

### APP ###
app:
	docker compose up -f ${APP_FILE} --detach --build

exec-app:
	docker exec -it ${NAME}-app /bin/bash

.PHONY: app exec-app
