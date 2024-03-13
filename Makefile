re: up

install:
	pip install -r requirements.txt

test:
	python -m pytest

lint:
	black myproject/*

build:
	docker-compose up --build

up: build
	docker-compose up

down:
	docker-compose down