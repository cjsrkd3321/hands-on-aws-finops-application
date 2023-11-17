from boto3.session import Session

from resources.base import LIST_FUNCS, DeleteResultType, TagResultType, Client
from items.item import Item, ItemBuilder
from items.state import State


def has_tag_key(tags: TagResultType, key: str) -> bool:
    for tag in tags:
        if tag["Key"] == key:  # type: ignore
            return True
    return False


def main() -> None:
    items: dict[str, Item] = {}  # 전역 변수로 선언하여 향후에 캐시로도 활용 가능!

    for service, list_func in LIST_FUNCS:
        for region in ["ap-northeast-2", "us-east-1", "us-west-1"]:
            sess: Client = Session().client(service_name=service, region_name=region)
            real_region: str = sess._client_config.region_name  # type: ignore
            cache_key: str = f"{real_region}!{list_func.__name__}"

            if cache_key in items:
                continue

            for result in list_func(sess):
                item: Item = (
                    ItemBuilder()
                    .set_resource(result)  # type: ignore
                    .set_region(real_region)
                    .set_type(result.__class__.__name__)
                    .build()
                )
                items[cache_key] = item

    for _, item in items.items():
        if has_tag_key(item.tags, "rex"):
            item.state, item.reason = State.FILTERED, Exception("TAG_KEY_FILTER")
            continue

        err: DeleteResultType = item.delete()
        if err:
            item.state, item.reason = State.FAILED, err
        else:
            item.state = State.DELETED

    for item in items.values():
        print(item)


if __name__ == "__main__":
    main()
