import argparse

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Stokholm", description="Do you wannacry ?")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument(
        "-k",
        "--key",
        default=False,
        action="store_true",
        help="Generate private and public key"
    )
    parser.add_argument(
        "-r",
        "--reverse",
        default=False,
        action="store_true",
        help="Reverse infected file to unencrypted"
    )
    parser.add_argument(
        "-s",
        "--silent",
        default=False,
        action="store_true",
        help="Silent any print output"
    )
    return parser.parse_args()
