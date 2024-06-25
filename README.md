# Junior Machine Learning and Platforms Engineer Tasks

## Task 1: Data Collection and Preprocessing

### Description

Use the following REST API endpoint to collect tax data: [Tax Data API](https://apilayer.com/marketplace/tax_data-api)  
`api_key = UYpBgbs9eoWYJne1c509FnyyRznkrxu3`  
Use method: `GET /us_rate_list`  
Sign up for an API key from the provided link and get the free plan.

### Requirements

1. Write a Python script to fetch the data from the API.
2. Perform data cleaning (handle missing values, remove duplicates, etc.).
3. Perform feature engineering (create new features, normalize/standardize data, etc.).
4. Save the processed data in MinIO in a suitable format (CSV, JSON, etc.). Preferred file format: Parquet.

## Task 2: Model Deployment

### Description

Use the provided pre-trained machine learning model: [Credit Card Fraud Detection Model](https://www.kaggle.com/models/nishikasingh/credit-card-fraud-detection)

### Requirements

1. Containerize the model using Docker.
2. Create an API endpoint using Flask or FastAPI to serve the model predictions.
3. Deploy the containerized model to a cloud platform (AWS, GCP, or Azure) or on a local machine.
4. Demonstrate how to test the deployed model using sample data.

## Task 3: Model Monitoring and Evaluation

### Description

Assume the deployed model from Task 2 is in production. The task involves setting up monitoring and evaluating its performance over time.

### Requirements

1. Set up logging to track requests and responses to the API endpoint.
2. Install MLflow and set up MLflow tracking.
3. Create a script to evaluate the model's performance on new data (e.g., calculating metrics like accuracy, precision, recall).
4. Explain the concept of data drift on a given model from Task 2.
