from concurrent import futures
from boto3.session import Session

from resources.base import LIST_FUNCS, Client, DeleteResultType
from items.item import Item, ItemBuilder
from items.state import State


ITEMS: dict[str, list[Item]] = {}


def lister(list_func, sess: Client, region: str) -> None:
    cache_key: str = f"{region}!{list_func.__name__}"

    if cache_key in ITEMS:
        return

    ITEMS[cache_key] = []
    for result in list_func(sess):
        ITEMS[cache_key].append(
            ItemBuilder()
            .set_resource(result)
            .set_region(region)
            .set_type(list_func.__name__)
            .build()
        )


def deleter(item: Item) -> tuple[Item, DeleteResultType]:
    return item, item.delete()


def main() -> None:
    threads: list = []

    pool = futures.ThreadPoolExecutor()

    for service, list_func in LIST_FUNCS:
        for region in ["ap-northeast-2", "us-east-1", "us-west-1"]:
            threads += [
                pool.submit(
                    lister,
                    list_func,
                    (
                        sess := Session().client(
                            service_name=service, region_name=region
                        )
                    ),
                    sess._client_config.region_name,  # type: ignore
                )
            ]

    futures.wait(fs=threads, return_when=futures.ALL_COMPLETED)

    threads.clear()

    threads += [
        pool.submit(deleter, item) for items in ITEMS.values() for item in items
    ]
    for future in futures.as_completed(threads):
        item, err = future.result()
        if err:
            item.state, item.reason = State.FAILED, err
        else:
            item.state = State.DELETED
        print(item)


if __name__ == "__main__":
    main()
