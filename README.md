# Python AWS Lambda

This is a simple AWS Lambda written in python. It returns an HTTP response including a randomly selected powerball value containing random numbers.

Use `Makefile` to install dependencies, test, format code, and build output.

In AWS - upload the `app.zip` file - set the handler to `src.lambda_handler.lambda_handler`