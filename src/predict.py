import joblib

# Load trained model
model = joblib.load("models/risk_classifier.pkl")

def predict_risk(text):
    prediction = model.predict([text])[0]
    return prediction