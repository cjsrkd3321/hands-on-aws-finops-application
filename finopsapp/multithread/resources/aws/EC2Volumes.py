from mypy_boto3_ec2 import EC2Client
from mypy_boto3_ec2.type_defs import VolumeTypeDef

from resources.base import (
    DeleteResultType,
    ListResultType,
    TagResultType,
    ResourceBase,
    LIST_FUNCS,
)


class EC2Volume(ResourceBase):
    def __init__(self, svc: EC2Client, volume: VolumeTypeDef) -> None:
        self.svc: EC2Client = svc
        self.volume = volume

    def delete(self) -> DeleteResultType:
        try:
            self.svc.delete_volume(VolumeId=self.volume["VolumeId"])
        except Exception as e:
            return e
        return None

    @property
    def tags(self) -> TagResultType:
        return self.volume.get("Tags", [])

    def __str__(self) -> str | None:
        return self.volume.get("VolumeId")


def list_ec2_volumes(sess: EC2Client) -> ListResultType:
    svc: EC2Client = sess
    iterator = svc.get_paginator("describe_volumes").paginate(
        Filters=[
            {
                "Name": "status",
                "Values": ["available"],
            }
        ]
    )

    return (
        EC2Volume(
            svc,
            volume,
        )
        for volumes in iterator
        for volume in volumes["Volumes"]
    )


if __name__ != "__main__":
    LIST_FUNCS.append(("ec2", list_ec2_volumes))  # type: ignore
