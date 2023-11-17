from abc import ABCMeta, abstractmethod
from typing import Callable, Generator, Literal
from mypy_boto3_ec2 import EC2Client


type Client = EC2Client
type Service = Literal["ec2"]
type DeleteResultType = Exception | None
type ListResultType = Generator[ResourceBase | None, None, None]
type ResourceType = tuple[Service, Callable[[Client], ListResultType]]
type TagType = dict[str, str]
type TagResultType = list[TagType | None]

LIST_FUNCS: list[ResourceType] = []


class ResourceBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, sess: Client) -> None:
        self.svc: Client = sess

    @abstractmethod
    def delete(self) -> DeleteResultType:
        pass

    @property
    @abstractmethod
    def tags(self) -> TagResultType:
        pass

    @abstractmethod
    def __str__(self) -> str | None:
        pass
