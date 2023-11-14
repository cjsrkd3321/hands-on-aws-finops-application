from boto3.session import Session

from resources.base import LIST_FUNCS, DeleteResultType
from items.item import Item, ItemBuilder
from items.state import State


def main() -> None:
    items: list[Item] = []

    for list_func in LIST_FUNCS:
        for region in ["ap-northeast-2"]:
            for result in list_func(Session(region_name=region)):
                items.append(
                    ItemBuilder()
                    .set_resource(result)  # type: ignore
                    .set_type(result.__class__.__name__)
                    .build()
                )

    for item in items:
        err: DeleteResultType = item.delete()
        if err:
            item.state, item.reason = State.FAILED, err
        else:
            item.state = State.DELETED
        print(item)


if __name__ == "__main__":
    main()
