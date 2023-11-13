from boto3.session import Session

from resources.base import LIST_FUNCS


def main() -> None:
    for list_func in LIST_FUNCS:
        for region in ["ap-northeast-2"]:
            for result in list_func(Session(region_name=region)):
                print(result.delete())  # type: ignore


if __name__ == "__main__":
    main()
