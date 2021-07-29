.PHONY: all install test format build verify deploy cleanup

APP_NAME=python-powerball-lambda

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

deploy:
	# create a simple stack with just s3 bucket first so we can upload the source code into the bucket
	if aws cloudformation describe-stacks --stack-name $(APP_NAME); then \
		echo "stack already exists, updating"; \
	else \
		echo "stack does not exist yet, creating"; \
		aws cloudformation create-stack --template-body file://aws/cloudformation.yaml \
			--stack-name $(APP_NAME) \
		    --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND \
		    --parameters ParameterKey=AppName,ParameterValue=$(APP_NAME) ParameterKey=BucketOnly,ParameterValue=true; \
		aws cloudformation wait stack-create-complete --stack-name $(APP_NAME); \
	fi;

	# copy source code .zip to new s3 bucket
	aws s3 cp dist/app.zip s3://$(APP_NAME)-bucket

	# update the stack (create lambda & roles)
	aws cloudformation update-stack --template-body file://aws/cloudformation.yaml \
		--stack-name $(APP_NAME) \
		--capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND \
		--parameters ParameterKey=AppName,ParameterValue=$(APP_NAME);
	aws cloudformation wait stack-update-complete --stack-name $(APP_NAME);
	aws cloudformation describe-stacks --stack-name python-powerball-lambda --query "Stacks[0].Outputs[0].OutputValue" | xargs curl

cleanup:
	aws s3 rm s3://$(APP_NAME)-bucket --recursive
	aws cloudformation delete-stack --stack-name $(APP_NAME)
	aws cloudformation wait stack-delete-complete --stack-name $(APP_NAME)
