from abc import ABCMeta, abstractmethod
from botocore.client import BaseClient
from typing import Callable, Generator
from boto3.session import Session


type DeleteResultType = Exception | None
type ListResultType = Generator[ResourceBase | None, None, None]
type ResourceType = Callable[[Session], Generator[ResourceBase | None, None, None]]


LIST_FUNCS: list[ResourceType] = []


class ResourceBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, sess: BaseClient) -> None:
        self.sess: BaseClient = sess

    @abstractmethod
    def delete(self) -> DeleteResultType:
        pass

    @abstractmethod
    def __str__(self) -> str | None:
        pass
