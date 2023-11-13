import concurrent.futures
import boto3


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=48) as executor:
        list(executor.map(do_stuff, range(3000)))


def do_stuff(i):
    boto3.client("secretsmanager")
    print(i)


if __name__ == "__main__":
    main()
