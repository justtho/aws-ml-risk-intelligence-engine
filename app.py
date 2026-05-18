import streamlit as st
import pandas as pd
from datetime import datetime
import os

from src.predict import predict_risk
from src.rag_pipeline import semantic_search, generate_case_summary
from src.evaluate_model import evaluate_model

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(page_title="AWS ML Risk Intelligence Engine")

st.title("AWS ML Risk Intelligence Engine")

st.write("AI-powered financial risk classification system")

# ---------------------------------------------------
# Logging Function
# ---------------------------------------------------

def log_prediction(input_text, prediction, summary):
    log_path = "logs/prediction_logs.csv"

    new_log = pd.DataFrame([{
        "timestamp": datetime.now(),
        "input_text": input_text,
        "prediction": prediction,
        "summary": summary
    }])

    if os.path.exists(log_path):
        new_log.to_csv(log_path, mode="a", header=False, index=False)
    else:
        new_log.to_csv(log_path, index=False)

# ---------------------------------------------------
# Risk Analysis Section
# ---------------------------------------------------

user_input = st.text_area(
    "Enter investigation note, email, or transaction summary"
)

if st.button("Analyze Risk"):
    if user_input.strip():

        prediction = predict_risk(user_input)

        similar_cases = semantic_search(user_input)

        summary = generate_case_summary(
            user_input,
            prediction,
            similar_cases
        )

        log_prediction(user_input, prediction, summary)

        st.success(f"Predicted Category: {prediction}")

        st.subheader("AI Risk Summary")

        st.write(summary)

    else:
        st.warning("Please enter some text.")

# ---------------------------------------------------
# Semantic Search Section
# ---------------------------------------------------

st.divider()

st.subheader("Semantic Search")

search_query = st.text_input("Search similar historical cases")

if st.button("Search Similar Cases"):

    if search_query.strip():

        results = semantic_search(search_query)

        for i, item in enumerate(results, start=1):

            st.write(f"### Result {i}")

            st.write(item["text"])

            st.caption(f"Category: {item['category']}")

    else:
        st.warning("Please enter a search query.")

# ---------------------------------------------------
# Model Evaluation Section
# ---------------------------------------------------

st.divider()

st.subheader("Model Evaluation")

if st.button("Show Model Metrics"):

    accuracy, report, matrix = evaluate_model()
  
    st.metric("Accuracy", f"{accuracy:.2%}")

    st.write("Classification Report.(Metrics are based on a synthetic MVP dataset for pipeline validation purposes.)")
    
    st.dataframe(
        pd.DataFrame(report).transpose()
    )

    st.write("Confusion Matrix. (Metrics are based on a synthetic MVP dataset for pipeline validation purposes.)")

    st.dataframe(
        pd.DataFrame(matrix)
    )

    st.caption(
        "Metrics are based on a synthetic MVP dataset for pipeline validation purposes."
    )