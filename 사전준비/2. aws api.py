from typing import List
from botocore.client import BaseClient
from mypy_boto3_ec2 import EC2Client
from mypy_boto3_ec2.paginator import _PageIterator
from mypy_boto3_ec2.type_defs import VolumeTypeDef, DescribeVolumesResultTypeDef

import boto3


ec2: EC2Client | BaseClient = boto3.client("ec2")
# ec2 = boto3.session.Session().client("ec2")

# 생성
ec2.create_volume(Size=1, AvailabilityZone="ap-northeast-2a")

# 조회
volumes: List[VolumeTypeDef] = ec2.describe_volumes()["Volumes"]
for volume in volumes:
    print(volume)
    # 삭제
    ec2.delete_volume(VolumeId=volume["VolumeId"])

# # paginator 활용
# iterator: _PageIterator[DescribeVolumesResultTypeDef] = ec2.get_paginator(
#     "describe_volumes"
# ).paginate()
# for volumes in iterator:
#     for volume in volumes["Volumes"]:
#         print(volume)
#         ec2.delete_volume(VolumeId=volume["VolumeId"])
