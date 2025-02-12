from colorama import Fore, Style
import os

def log_title(title: str) -> None:
    is_silent = os.environ.get('STOCKHOLM_IS_SILENT')
    if not eval(is_silent):
        print(Fore.MAGENTA + title + Style.RESET_ALL)

def log_info(message: str, key: str = None) -> None:
    is_silent = os.environ.get('STOCKHOLM_IS_SILENT')
    if not eval(is_silent):
        if key:
            print(Fore.CYAN + key + Style.RESET_ALL, end=" ")
        print(message)


def log_error(error: str) -> None:
    is_silent = os.environ.get('STOCKHOLM_IS_SILENT')
    if not eval(is_silent):
        print(Fore.RED, end="")
        print(error, end="")
        print(Style.RESET_ALL)
        # print(message)