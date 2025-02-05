#!/usr/bin/env python3
""" HOTP program """

import base64
import hmac
import hashlib
import time
import argparse

class HOTP:
    """ HOTP operation """
    HTOP_DIGIT = 6 # HTOP code digit length
    HTOP_COUNTER = int(time.time())//30 # Counter message depend on time 30 second

    def __init__(self, filename):
        self.key_file = filename


    def generate_key(self, filename):
        """ Generate key file from Hex secret """
        try:
            content = self.__read_hex_secret(filename)
            key = base64.b32encode(bytes(content, 'utf-8'))
            with open(self.key_file, 'wb') as file:
                file.write(key)
                print(f"Key was successfully saved in {self.key_file}.")
        except Exception as e:
            print(e)

    def generate_hotp(self, filename):
        """ Generate HOTP base on 30s with SHA256 """
        file = open(filename, 'rb')
        key = base64.b32decode(file.read())
        h = hmac.new(key, self.HTOP_COUNTER.to_bytes(8, byteorder="big"), hashlib.sha256).digest()
        code = self.__truncate_code(h)
        return code

    def __is_hex(self, s):
        """ Validate string is hexadecimal """
        try:
            _ = int(s,16)
            return True
        except ValueError:
            return False

    def __read_hex_secret(self, filename):
        """ Read secret file and validate """
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if len(content) != 64 or not self.__is_hex(content):
                raise Exception("error: key must be 64 hexadecial characters")
            return content

    def __truncate_code(self, hash):
        """ Trancate hash to code """
        i = hash[-1] % 16
        truncated = int.from_bytes(hash[i:i + 4], byteorder = 'big', signed = False) % 2 ** 31
        code = truncated % 10 ** self.HTOP_DIGIT
        return code

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

def main():
    """ Main """
    args = optparsing()
    print('args:', args)
    hotp = HOTP(args.output)
    if args.generate:
        hotp.generate_key(args.generate)
    if args.key:
        code = hotp.generate_hotp(args.key)
        print(code)

if __name__ == '__main__':
    main()
