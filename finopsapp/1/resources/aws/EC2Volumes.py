import boto3
from mypy_boto3_ec2 import EC2Client
from mypy_boto3_ec2.type_defs import VolumeTypeDef

from resources.base import (
    LIST_FUNCS,
    ListResultType,
    DeleteResultType,
    ResourceBase,
)


class EC2Volume(ResourceBase):
    def __init__(self, sess: EC2Client, volume: VolumeTypeDef) -> None:
        self.sess: EC2Client = sess
        self.volume = volume

    def delete(self) -> DeleteResultType:
        try:
            self.sess.delete_volume(VolumeId=self.volume["VolumeId"])
        except Exception as e:
            return e
        return None

    def __str__(self) -> str | None:
        return self.volume.get("VolumeId")


def list_ec2_volumes(region="ap-northeast-2") -> ListResultType:
    sess: EC2Client = boto3.client("ec2", region_name=region)
    iterator = sess.get_paginator("describe_volumes").paginate(
        Filters=[
            {
                "Name": "status",
                "Values": ["available"],
            }
        ]
    )

    return (
        EC2Volume(
            sess,
            volume,
        )
        for volumes in iterator
        for volume in volumes["Volumes"]
    )


if __name__ != "__main__":
    LIST_FUNCS.append(list_ec2_volumes)
