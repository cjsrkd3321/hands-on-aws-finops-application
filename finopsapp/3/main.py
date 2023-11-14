from boto3.session import Session

from resources.base import LIST_FUNCS, DeleteResultType
from items.item import Item
from items.state import State


def main() -> None:
    items: list[Item] = []

    for list_func in LIST_FUNCS:
        for region in ["ap-northeast-2"]:
            for result in list_func(Session(region_name=region)):
                items.append(Item(result, region, result.__class__.__name__))

    for item in items:
        err: DeleteResultType = item.delete()
        if err:
            item.state, item.reason = State.FAILED, err
        else:
            item.state = State.DELETED
        print(item)


if __name__ == "__main__":
    main()
