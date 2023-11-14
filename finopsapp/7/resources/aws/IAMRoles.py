from mypy_boto3_iam import IAMClient
from mypy_boto3_iam.type_defs import RoleTypeDef

from resources.base import (
    DeleteResultType,
    ListResultType,
    TagType,
    ResourceBase,
    LIST_FUNCS,
)


class IAMRole(ResourceBase):
    def __init__(self, svc: IAMClient, role: RoleTypeDef) -> None:
        self.svc: IAMClient = svc
        self.role = role

    def delete(self) -> DeleteResultType:
        try:
            self.svc.delete_role(RoleName=self.role["RoleName"])
        except Exception as e:
            return e
        return None

    @property
    def tags(self) -> list[TagType]:
        return self.role.get("Tags", [])

    def __str__(self) -> str:
        return self.role["RoleName"]


def list_iam_roles(sess: IAMClient) -> ListResultType:
    svc: IAMClient = sess
    iterator = svc.get_paginator("list_roles").paginate(
        PathPrefix="/rextest/",
    )

    return (
        IAMRole(
            svc,
            role,
        )
        for roles in iterator
        for role in roles["Roles"]
    )


if __name__ != "__main__":
    LIST_FUNCS.append(("iam", list_iam_roles))  # type: ignore
