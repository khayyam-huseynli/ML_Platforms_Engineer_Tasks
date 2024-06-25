# Building and Running `my_model_app` Docker Application

## Introduction

This guide will help you build and run the `my_model_app` Docker container, and make POST requests using Insomnia or Postman.

## Prerequisites

- Docker installed on your machine.
- Insomnia or Postman installed for making API requests.

## Building the Docker Image

To build the Docker image for `my_model_app`, use the following command:

`docker build -t my_model_app`


This command will create a Docker image with the tag my_model_app based on the Dockerfile in your current directory.


## Running the Docker Container

To run the Docker container and expose it on port 5000, use the following command:


`docker run -p 5000:5000 my_model_app`

This command will start the container and map port 5000 on your host to port 5000 on the container.

## Making POST Requests

## Using Insomnia

1. Open Insomnia.
2. Create a new POST request.
3. Set the request URL to:

   `http://localhost:5000/predict`

   Add the required request body in JSON format. For example

   {
    "Time": -1.1152878574425795,
    "V1": -19.1397328634111,
    "V2": 9.28684735978866,
    "V3": -20.134992104854,
    "V4": 7.81867331002574,
    "V5": -15.652207677206302,
    "V6": -1.66834770694329,
    "V7": -21.3404780994803,
    "V8": 0.6418997011947,
    "V9": -8.55011032700099,
    "V10": -16.6496281595399,
    "V11": 4.81815244707108,
    "V12": -9.44531478308794,
    "V13": 1.3170562933234098,
    "V14": -7.24346097400378,
    "V15": 0.830910291033798,
    "V16": -9.533257050393189,
    "V17": -18.750641147467398,
    "V18": -8.09264877340557,
    "V19": 3.32675827497024,
    "V20": 0.42720343146936,
    "V21": -2.1826919456095504,
    "V22": 0.5205430723666421,
    "V23": -0.7605564151887328,
    "V24": 0.6627666383972359,
    "V25": -0.948454306235033,
    "V26": 0.12179592582979301,
    "V27": -3.3818429293561,
    "V28": -1.2565236213625801,
    "Amount": 0.20610286556509647
   }
