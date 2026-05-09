from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("heart.csv")

X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Heart Disease Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json.get("features")
        prediction = model.predict([data])[0]
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
