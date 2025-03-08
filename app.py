from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
from model import predict_fraud

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(request.form[f'feature{i}']) for i in range(30)]
        prediction = predict_fraud(np.array([data]))
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
