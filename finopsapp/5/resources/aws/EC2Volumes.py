from boto3.session import Session
from mypy_boto3_ec2 import EC2Client
from mypy_boto3_ec2.type_defs import VolumeTypeDef

from resources.base import (
    DeleteResultType,
    ListResultType,
    TagType,
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
    def tags(self) -> list[TagType]:
        return self.volume.get("Tags", [])

    def __str__(self) -> str | None:
        return self.volume.get("VolumeId")


def list_ec2_volumes(sess: Session) -> ListResultType:
    svc: EC2Client = sess.client(service_name="ec2")
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
    LIST_FUNCS.append(list_ec2_volumes)
