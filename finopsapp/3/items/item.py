from typing import TypedDict

from items.state import State
from resources.base import ResourceBase, DeleteResultType


class ItemDict(TypedDict):
    state: State
    reason: Exception | None
    region: str
    resource: ResourceBase | None
    type: str


class Item:
    def __init__(self, resource: ResourceBase | None, region: str, name: str) -> None:
        self.__item: ItemDict = {
            "state": State.NEW,
            "reason": None,
            "region": region,
            "resource": resource,
            "type": name,
        }

    def delete(self) -> DeleteResultType:
        return self.__item["resource"].delete()  # type: ignore

    @property
    def state(self) -> State:
        return self.__item["state"]

    @state.setter
    def state(self, value: State) -> None:
        self.__item["state"] = value

    @property
    def reason(self) -> Exception | None:
        return self.__item["reason"]

    @reason.setter
    def reason(self, value: Exception) -> None:
        self.__item["reason"] = value

    def __str__(self) -> str:
        return f"{self.__item['region']} - {self.__item['type']} - {self.__item['resource']} | {self.__item['state']} - {self.__item['reason']}"
