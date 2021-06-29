.PHONY: setup test format build

setup:
	pipx install pipenv
	pipenv install --pre -d

test:
	pipenv run pytest --cov=src

format:
	pipenv run isort .
	pipenv run black .

build:
	pipenv lock --pre
	mkdir -p dist
	zip dist/app.zip src -r