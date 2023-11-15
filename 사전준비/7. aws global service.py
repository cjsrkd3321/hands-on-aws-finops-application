import boto3

regions = ["ap-northeast-2", "us-east-1", "us-west-1"]
services = ["ec2", "iam", "cloudfront", "lambda"]

no_duplicated = []

for service in services:
    for region in regions:
        svc = boto3.client(service_name=service, region_name=region)  # type: ignore
        real_region = svc._client_config.region_name

        list_value = f"{service}!{real_region}"
        if list_value in no_duplicated:
            continue

        print(service, region, svc._client_config.region_name)
        no_duplicated.append(list_value)
