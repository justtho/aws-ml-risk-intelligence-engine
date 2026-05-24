import json
import boto3
from aws_utils.config import AWS_REGION

BEDROCK_MODEL_ID = "us.meta.llama3-3-70b-instruct-v1:0"

def generate_bedrock_summary(text, prediction, similar_cases):

    bedrock = boto3.client(
        service_name="bedrock-runtime",
        region_name=AWS_REGION
    )

    context = "\n".join(
        [f"- {case['text']} | Category: {case['category']}" for case in similar_cases]
    )

    prompt = f"""
You are an AI risk analyst. Your task is to analyze ONLY the new case.

Do not repeat the similar historical cases.
Do not copy text from the similar cases.
Use the similar cases only as reference context.

Return the response exactly in this format:

Summary:
<maximum 2 short sentences about the new case>

Risk Category:
{prediction}

Key Indicators:
- <indicator 1 from the new case>
- <indicator 2 from the new case>

Recommended Action:
<one short recommended next step>

New Case:
{text}

Reference Similar Cases:
{context}
"""

    body = {
        "prompt": prompt,
        "max_gen_len": 150,
        "temperature": 0.1,
        "top_p": 0.7,
        "stop": ["Here is the rewritten response"]
    }

    response = bedrock.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        body=json.dumps(body)
    )

    response_body = json.loads(
        response["body"].read()
    )

    output = response_body["generation"]

    if "Here is the rewritten response" in output:
       output = output.split("Here is the rewritten response")[0]

    return output.strip()