.PHONY: all install test format build verify

all: format test verify build

install:
	pip install pipenv
	pipenv install --pre -d

test:
	pipenv run pytest --cov=src --cov-fail-under=80

format:
	pipenv run isort .
	pipenv run black .

build:
	pipenv lock --pre
	mkdir -p dist
	zip dist/app.zip src -r

verify:
	pipenv run flake8 .