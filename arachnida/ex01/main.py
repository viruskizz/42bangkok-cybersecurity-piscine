"""
_summary_
"""

import argparse

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Spider", description="scaping image from web")
    parser.add_argument("urls", nargs="*")
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_false",
        help="recursively downloads the images in a URL received as a parameter"
    )
    parser.add_argument(
        "-l",
        "--level",
        type=int,
        default=5,
        help="indicates the maximum depth level of the recursive download, default 5"
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default="./data/",
        help="The path where the downloaded files will be saved, default ./data/"
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = optparsing()
    print(args)
    