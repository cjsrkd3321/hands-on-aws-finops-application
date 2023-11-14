import boto3

regions = ["ap-northeast-2", "us-east-1", "us-west-1"]
services = ["ec2", "iam", "cloudfront", "lambda"]

for service in services:
    for region in regions:
        svc = boto3.client(service_name=service, region_name=region)  # type: ignore
        print(service, region, svc._client_config.region_name)
