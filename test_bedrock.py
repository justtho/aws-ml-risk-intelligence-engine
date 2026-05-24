from aws_utils.bedrock_summary import generate_bedrock_summary

sample_text = "Customer reported an unauthorized wire transfer and requested urgent investigation."
prediction = "Fraud"

similar_cases = [
    {
        "text": "Customer reported unauthorized transaction on account",
        "category": "Fraud"
    },
    {
        "text": "Suspicious login attempt detected from foreign IP",
        "category": "Fraud"
    }
]

summary = generate_bedrock_summary(
    sample_text,
    prediction,
    similar_cases
)

print(summary)