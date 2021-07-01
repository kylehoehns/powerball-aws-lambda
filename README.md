# Python AWS Lambda

This is a simple AWS Lambda written in python. It returns an HTTP response including a randomly selected powerball value containing random numbers.

## Running and Tests
* `make install` - Installs dependencies
* `make all` - formats code, runs tests, verifies code style, and builds the output .zip file

## Deploying to AWS
* Download and configure [AWS cli](https://aws.amazon.com/cli/) using your AWS credentials
* `make deploy`
  *  If you want to use a different name than `python-powerball-lambda` that can be edited at the top of the `Makefile`