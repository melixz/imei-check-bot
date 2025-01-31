.PHONY: install up down restart logs api bot

install:
	poetry install

up:
	docker-compose up -d

down:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f

api:
	docker-compose up -d api

bot:
	docker-compose up -d bot