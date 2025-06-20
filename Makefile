SOURCE=./src
DOCKER=./docker

DJANGO_SETTINGS_MODULE=config.settings.local

DJANGO_SETTINGS = --settings=$(DJANGO_SETTINGS_MODULE)


init:
	export PYTHONPATH=$(PWD):$(PWD)/src

run.docker:
	docker-compose -f ./.docker/docker-compose.yml up

run.local:
	python $(SOURCE)/manage.py runserver 0.0.0.0:8000 $(DJANGO_SETTINGS)

# Django Command

migrations: init
	python ./src/manage.py makemigrations $(DJANGO_SETTINGS)

migrate:
	python ./src/manage.py migrate $(DJANGO_SETTINGS)