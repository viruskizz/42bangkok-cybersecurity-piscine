#!/usr/bin/env python3
""" TOTP program """

import base64
import hmac
import hashlib
import time
import argparse

KEY_FILE = ''
HTOP_DIGIT = 6 # HTOP code digit length
HTOP_COUNTER = int(time.time())//30 # Counter message depend on time 30 second

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Spider", description="scaping image from web")
    parser.add_argument("file", nargs="*")
    parser.add_argument(
        "-g",
        "--generate",
        help="Generate Hex key to secret"
    )
    parser.add_argument(
        "-k",
        "--key",
        help="Generate OTP from secret key"
    )
    parser.add_argument(
        '-o',
        "--output",
        default='ft_otp.key',
        help="Output to file",
    )
    return parser.parse_args()

def is_hex(s):
    """ Validate string is hexadecimal """
    try:
        _ = int(s,16)
        return True
    except ValueError:
        return False

def read_hex_secret(filename):
    """ Read secret file and validate """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        if len(content) != 64 or not is_hex(content):
            raise Exception("error: key must be 64 hexadecial characters")
        return content

def generate_key(filename):
    """ Generate key file from Hex secret """
    try:
        content = read_hex_secret(filename)
        key = base64.b32encode(bytes(content, 'utf-8'))
        with open(KEY_FILE, 'wb') as file:
            file.write(key)
            print(f"Key was successfully saved in {KEY_FILE}.")
    except Exception as e:
        print(e)

def truncate_code(hash):
    """ Trancate hash to code """
    i = hash[-1] % 16
    truncated = int.from_bytes(hash[i:i + 4], byteorder = 'big', signed = False) % 2 ** 31
    code = truncated % 10 ** HTOP_DIGIT
    return code

def generate_hotp(filename):
    """ Generate HOTP base on 30s with SHA256 """
    file = open(filename, 'rb')
    key = base64.b32decode(file.read())
    h = hmac.new(key, HTOP_COUNTER.to_bytes(8, byteorder="big"), hashlib.sha256).digest()
    code = truncate_code(h)
    return code


if __name__ == '__main__':
    args = optparsing()
    print('args:', args)
    KEY_FILE = args.output
    if args.generate:
        generate_key(args.generate)
    if args.key:
        hotp = generate_hotp(args.key)
        print(hotp)