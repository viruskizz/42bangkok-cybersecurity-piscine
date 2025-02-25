NAME=vaccine
APP_DIR=app
DVWA_DIR=dvwa

$(NAME): all

all: up

up: dvwa app

dev: dev-app

down: down-app down-dvwa

clean: clean-app clean-dvwa

fclean: fclean-app fclean-dvwa

re: down up

.PHONY: up down stop clean fclean re

### APP ###
app:
	make -C ${APP_DIR}

dev-app:
	make -C ${APP_DIR} dev

exec-app:
	make -C ${APP_DIR} exec

stop-dvwa:
	make -C ${APP_DIR} stop

down-dvwa:
	make -C ${APP_DIR} down

fclean-dvwa:
	make -C ${APP_DIR} fclean

rmdir:
	docker run --rm -v "$(PWD):/app" -w /app alpine rm -rf dvwa/mydata dvwa/pgdata

.PHONY: app exec-app stop-app down-app

### DVWA ###
dvwa:
	make -C ${DVWA_DIR} up

exec-dvwa:
	make -C ${DVWA_DIR} exec

stop-dvwa:
	make -C ${DVWA_DIR} stop

down-dvwa:
	make -C ${DVWA_DIR} down

fclean-dvwa:
	make -C ${DVWA_DIR} fclean

.PHONY: dvwa exec-dvwa stop-dvwa down-dvwa
