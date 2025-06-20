SOURCE=./src
DOCKER=./docker

DJANGO_SETTINGS_MODULE=config.settings.local

DJANGO_SETTINGS = --settings=$(DJANGO_SETTINGS_MODULE)

run.docker:
	docker-compose -f ./.docker/docker-compose.yml up

run.local:
	python $(SOURCE)/manage.py runserver 0.0.0.0:8000 $(DJANGO_SETTINGS)

# Django Command

migrations:
	python $(SOURCE)/manage.py makemigrations $(DJANGO_SETTINGS)

migrate:
	python $(SOURCE)/manage.py migrate $(DJANGO_SETTINGS)