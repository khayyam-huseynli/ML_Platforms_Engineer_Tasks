# Building and Running `my_mlflow_app` Docker Application

## Introduction

This guide will help you build and run the `my_mlflow_app` Docker container, set up the MLflow UI, and make POST requests using Insomnia or Postman.

## Prerequisites

- Docker installed on your machine.
- Insomnia or Postman installed for making API requests.
- MLflow installed. You can install it using pip:
  ```bash
  pip install mlflow

## Building the Docker Image

To build the Docker image for my_mlflow_app, use the following command:

  `docker build -t my_mlflow_app`

This command will create a Docker image with the tag my_mlflow_app based on the Dockerfile in your current directory.

## Setting Up MLflow UI

To start the MLflow UI, use the following command:

  `mlflow ui`

This command will start the MLflow tracking UI, typically available at http://localhost:5000.

## Running the Docker Container

To run the Docker container, expose it on port 8000, mount a volume for logs, and set the MLflow tracking URI, use the following command:

  `docker run -p 8000:8000 -v ./logs:/logs -e MLFLOW_TRACKING_URI=http://host.docker.internal:5000 my_mlflow_app`

This command will start the container, map port 8000 on your host to port 8000 on the container, and set the MLflow tracking URI to the MLflow UI running on your host.

