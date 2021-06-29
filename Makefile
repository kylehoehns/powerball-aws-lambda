
.PHONY: setup test format

setup:
	pipx install pipenv
	pipenv install --pre -d

test:
	pytest

format:
	pipenv run isort .
	pipenv run black .

build:
	mkdir dist
	zip dist/app.zip src -r
