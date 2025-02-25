import os
import time
import argparse
import tarfile
from requests.exceptions import HTTPError
import requests
import yaml

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
        default='output.tar',
        action="store_false",
        help="save result to output"
    )
    parser.add_argument(
        "-H",
        "--header",
        action='append',
        help="add metadata EXIF file"
    )
    return parser.parse_args()

def take_vaccine():
    with open("payload.list.yml") as f:
        vaccine_list = yaml.safe_load(f)
        for db, values in vaccine_list.items():
            print(f'Take vaccine on database {db}')
            for type, queries in values.items():
                print(f'tring on {type} type')
                for index, q in enumerate(queries):
                    # make_request(q)
                    query_name = f"{db}-{type}-{index}"
                    print(query_name)
                    response = make_request(q)
                    output(query_name, response)
                    time.sleep(0.5)

def make_request_headers():
    headers = {}
    if args.header and len(args.header) > 0:
        for h in args.header:
            key,value = h.split("=")
            headers[key] = value
    return headers

def make_request(query: str):
    try:
        headers = make_request_headers()
        print(headers)
        if args.request.upper() == 'POST':
            r = requests.post(args.url, headers=headers)
        else:
            r = requests.get(args.url, headers=headers)
        if r.status_code == 200:
            return r.text
        else:
            return r.reason
    except HTTPError as e:
        print(e.response.text)
    except Exception as e:
        print(e)

def output(name: str, result: str):
    try:
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = os.path.join(output_dir, name)
        with open(filename, 'w') as f:
            f.write(result)
    except Exception as e:
        print(e)

def make_achive():
    try:
        filename = args.output
        target_dir = 'output'
        with tarfile.open(filename, "w") as tar:
            for root, dirs, files in os.walk(target_dir):
                for f in files:
                    tar.add(os.path.join(root, f))
        print(f'Archive output to {filename}')
    except Exception as e:
        print(e)

def main():
    take_vaccine()
    make_achive()

if __name__ == '__main__':
    args = optparsing()
    print(args)
    main()