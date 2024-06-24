from flask import Flask, request, jsonify
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib
import logging
import mlflow
import mlflow.sklearn
import pandas as pd
from datetime import datetime

# Set the MLflow tracking URI to the host machine's MLflow server
mlflow.set_tracking_uri("http://host.docker.internal:5000")

# Set the experiment name
experiment_name = "Fraud_detection_Experiment"

# Create experiment if it doesn't exist
if not mlflow.get_experiment_by_name(experiment_name):
    experiment_id = mlflow.create_experiment(experiment_name)

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='/logs/api_requests.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# Load the pre-trained model
model = joblib.load('fraud-model_v1.pk')

@app.before_request
def log_request_info():
    logging.info(f"Request: {request.method} {request.url} {request.data}")

@app.after_request
def log_response_info(response):
    logging.info(f"Response: {response.status} {response.data}")
    return response

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame.from_dict(data, orient='index').T
    features = df.drop('Class', axis=1)
    y_true = df['Class']
    y_pred = model.predict(features)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_true, y_pred)

    # Calculate precision
    precision = precision_score(y_true, y_pred)

    # Calculate recall
    recall = recall_score(y_true, y_pred) 
    
          
    # Log prediction details to MLFlow
    with mlflow.start_run(run_name='lr_model', experiment_id=experiment_id) as run:
        mlflow.sklearn.log_model(model, "fraud_detection_model")
        mlflow.log_param("request_timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        mlflow.log_param("features", data)
        mlflow.log_metric("prediction", y_pred[0])
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
    
    response = {"prediction": y_pred.tolist()}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
