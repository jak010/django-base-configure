
SRC=./src
DOCKER=./docker

run.local:
	python $(SRC)/manage.py runserver 0.0.0.0:8000 --settings=config.settings.local

run.docker:
	docker-compose -f ./.docker/docker-compose.yml up

