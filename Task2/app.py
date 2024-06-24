from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('fraud-model_v1.pk')

@app.route('/')
def home():
	return "Hello"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = pd.DataFrame.from_dict(data, orient='index').T
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)