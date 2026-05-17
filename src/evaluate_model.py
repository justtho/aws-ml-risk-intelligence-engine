import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def evaluate_model():
    df = pd.read_csv("data/sample_cases.csv")

    X = df["text"]
    y = df["category"]

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = joblib.load("models/risk_classifier.pkl")
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)
    matrix = confusion_matrix(y_test, predictions)

    return accuracy, report, matrix