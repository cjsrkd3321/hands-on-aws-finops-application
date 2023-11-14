from boto3.session import Session

from resources.base import LIST_FUNCS, DeleteResultType, TagType, Client
from items.item import Item, ItemBuilder
from items.state import State


def has_tag_key(tags: list[TagType], key: str) -> bool:
    for tag in tags:
        if tag["Key"] == key:
            return True
    return False


def main() -> None:
    items: list[Item] = []

    for service, list_func in LIST_FUNCS:
        for region in ["ap-northeast-2", "us-east-1"]:
            sess: Client = Session().client(service_name=service, region_name=region)
            for result in list_func(sess):
                items.append(
                    ItemBuilder()
                    .set_resource(result)  # type: ignore
                    .set_type(result.__class__.__name__)
                    .build()
                )

    for item in items:
        if has_tag_key(item.tags, "rex"):
            item.state, item.reason = State.FILTERED, Exception("TAG_KEY_FILTER")
            continue

        err: DeleteResultType = item.delete()
        if err:
            item.state, item.reason = State.FAILED, err
        else:
            item.state = State.DELETED

    for item in items:
        print(item)


if __name__ == "__main__":
    main()
