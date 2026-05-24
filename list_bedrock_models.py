import boto3
from aws_utils.config import AWS_REGION

client = boto3.client("bedrock", region_name=AWS_REGION)

response = client.list_foundation_models(
    byOutputModality="TEXT"
)

for model in response["modelSummaries"]:
    lifecycle = model.get("modelLifecycle", {}).get("status", "UNKNOWN")
    print(
        lifecycle,
        "|",
        model["providerName"],
        "|",
        model["modelName"],
        "|",
        model["modelId"]
    )