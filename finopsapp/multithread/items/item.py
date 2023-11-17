from typing import Self

from items.state import State
from resources.base import ResourceBase, DeleteResultType, TagResultType
from resources.utils import convert_dict_to_tags


class Item:
    def __init__(self) -> None:
        self.state: State = State.NEW
        self.reason: Exception | None = None
        self.region: str = "ap-northeast-2"
        self.resource: ResourceBase
        self.type: str | None = None

    def delete(self) -> DeleteResultType:
        return self.resource.delete()

    @property
    def tags(self) -> TagResultType:
        return convert_dict_to_tags(self.resource.tags)

    def __str__(self) -> str:
        return f"{self.region} - {self.type} - {self.resource} | {self.state} - {self.reason}"


class ItemBuilder:
    def __init__(self) -> None:
        self.__item = Item()

    def set_state(self, state: State) -> Self:
        self.__item.state = state
        return self

    def set_reason(self, reason: DeleteResultType) -> Self:
        self.__item.reason = reason
        return self

    def set_resource(self, resource: ResourceBase) -> Self:
        self.__item.resource = resource
        self.__item.region = self.__item.resource.svc._client_config.region_name  # type: ignore
        return self

    def set_region(self, region: str) -> Self:
        self.__item.region = region
        return self

    def set_type(self, type: str | None) -> Self:
        self.__item.type = type
        return self

    def build(self) -> Item:
        return self.__item
