import argparse

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Inquisitor", description="ARP poisoning in the middle attack")
    parser.add_argument(
        "url",
        help="IP address of source"
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
        help="Archive file"
    )
    return parser.parse_args()

def main():
    print("Hello")

if __name__ == '__main__':
    args = optparsing()
    print(args)
    main()