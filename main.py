from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# 1. Load the model and scaler at startup
try:
    model = joblib.load('insurance_model.joblib')
    scaler = joblib.load('scaler.joblib')
    print("Model and Scaler loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")

@app.route('/', methods=['GET'])
def home():
    return "Insurance Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 2. Receive JSON data from the request
        data = request.get_json()

        # 3. Extract features in the correct order
        # Ensure the frontend sends these exact keys
        features = [
            data['Age'], data['Diabetes'], data['BloodPressureProblems'],
            data['AnyTransplants'], data['AnyChronicDiseases'], data['Height'],
            data['Weight'], data['KnownAllergies'], data['HistoryOfCancerInFamily'],
            data['NumberOfMajorSurgeries']
        ]

        # 4. Calculate BMI (Logic moved to backend for consistency)
        height_m = data['Height'] / 100
        bmi = data['Weight'] / (height_m ** 2)
        features.append(bmi)

        # 5. Reshape and Scale
        features_array = np.array([features])
        scaled_features = scaler.transform(features_array)

        # 6. Predict
        prediction = model.predict(scaled_features)

        # 7. Return the result as JSON
        return jsonify({
            'status': 'success',
            'prediction': round(float(prediction[0]), 2),
            'bmi': round(bmi, 2)
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    # host='0.0.0.0' is REQUIRED for Docker
    app.run(host='0.0.0.0', port=5000, debug=True)