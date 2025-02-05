#!/usr/bin/env python3
""" HOTP program """

import base64
import hmac
import hashlib
import time
import argparse
import segno
from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits, Header
from textual.containers import Center, Middle, Horizontal
from textual.timer import Timer

class HOTP:
    """ HOTP operation """
    HTOP_DIGIT = 6 # HTOP code digit length
    HTOP_COUNTER = int(time.time())//30 # Counter message depend on time 30 second

    def __init__(self, filename):
        self.key_file = filename

    def generate_key(self, filename):
        """ Generate key file from Hex secret """
        content = self.__read_hex_secret(filename)
        key = base64.b32encode(bytes(content, 'utf-8'))
        with open(self.key_file, 'wb') as file:
            file.write(key)
            print(f"Key was successfully saved in {self.key_file}.")

    def generate_hotp(self, filename, counter=int(time.time())//30):
        """ Generate HOTP base on 30s with SHA256 """
        bkey = self.__read_key_binary_file(filename)
        key = base64.b32decode(bkey)
        h = hmac.new(key, counter.to_bytes(8, byteorder="big"), hashlib.sha256).digest()
        code = self.__truncate_code(h)
        return code

    def create_uri(self, filename):
        """
        Create uri
        Example: otpauth://totp/{NAME}?secret={SECRET}>&algorithm=<<ALGO>>
        """
        file = open(filename, "r", encoding='utf-8')
        key = file.read()
        name = "example"
        issuer = 'ft_otp'
        uri = f"otpauth://totp/{issuer}:{name}?secret={key}&issuer={issuer}&algorithm=SHA256&digits=6&period=30"
        return uri

    def create_qrcode_uri(self, filename):
        uri = self.create_uri(filename)
        img = segno.make(uri)
        img.save('ft_otp.png', scale=3)

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

    def __read_key_binary_file(self, filename):
        with open(filename, "rb") as file:
            return file.read()

    def __truncate_code(self, hash):
        """ Trancate hash to code """
        i = hash[-1] % 16
        truncated = int.from_bytes(hash[i:i + 4], byteorder = 'big', signed = False) % 2 ** 31
        code = truncated % 10 ** self.HTOP_DIGIT
        return f"{code :06d}"

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
    parser.add_argument(
        "-q",
        "--qrcode",
        help="Generate QRCode uri from secret file"
    )
    parser.add_argument(
        "-i",
        "--interactive",
        help="Interactive code"
    )
    return parser.parse_args()


class ClockApp(App):
    CSS = """
    Horizontal {
        align: center middle;
    }
    #code {
        width: auto;
        text-style: bold;
        margin: 1
    }
    #counter {
        width: auto;
        padding: 0 2;
        border: solid yellow;
        margin-left: 2
    }
    """

    # progress_timer: Timer
    BINDINGS = [("s", "start", "Start")]
    counter_timer: Timer
    hotp: HOTP
    key_file: str
    code: str

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Digits("", id="code")
            yield Digits("", id="counter")

    def on_mount(self) -> None:
        """Set up a timer to simulate progess happening."""
        self.title = "FT Authenticator"
        self.code = self.hotp.generate_hotp(self.key_file)

    def on_ready(self) -> None:
        self.query_one("#code").update(self.code)
        self.update_clock()
        self.counter_timer = self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = int(time.time())
        if clock % 30 == 0:
            self.code = self.hotp.generate_hotp(self.key_file, clock//30)
            self.query_one("#code").update(self.code)
        self.query_one("#counter").update(f"{30 - clock % 30}")


def main():
    """ Main """
    args = optparsing()
    hotp = HOTP(args.output)
    try:
        if args.generate:
            hotp.generate_key(args.generate)
        elif args.key:
            code = hotp.generate_hotp(args.key)
            print(code)
        elif args.qrcode:
            hotp.create_qrcode_uri(args.qrcode)
        elif args.interactive:
            app = ClockApp()
            app.hotp = hotp
            app.key_file = args.interactive
            app.run()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
