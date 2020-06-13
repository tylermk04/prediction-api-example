# Prediction API

## Overview

- `./api `
  - `train.R` trains a rudimentary glmnet model on the mtcars dataset
  - `api.R` defines a basic API to predict MPG
- `./app`
  - `app.py` defines a single-page web app that predicts MPG for the given form values

## Usage

To run the application, simply run `docker-compose up` and navigate to `localhost:5000`.