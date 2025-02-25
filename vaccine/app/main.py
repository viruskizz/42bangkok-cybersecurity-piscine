import argparse
import requests
import yaml
import time

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="vaccine", description="Take viccine to website with SQL Injection")
    parser.add_argument(
        "url",
        help="URL of target"
    )
    parser.add_argument(
        "-X",
        "--request",
        default='get',
        help="Archive file"
    )
    parser.add_argument(
        "-o",
        "--output",
        default=True,
        action="store_false",
        help="save result to output"
    )
    return parser.parse_args()

def take_vaccine():
    with open("payload.list.yml") as f:
        vaccine_list = yaml.safe_load(f)
        for db, values in vaccine_list.items():
            print(f'Take vaccine on database {db}')
            for type, queries in values.items():
                print(f'tring on {type} type')
                for q in queries:
                    make_request(q)
                    time.sleep(0.5)


def make_request(query: str):
    if args.request.upper() == 'POST':
        r = requests.post(args.url)
    else:
        r = requests.get(args.url)

def main():
    take_vaccine()

if __name__ == '__main__':
    args = optparsing()
    print(args)
    main()