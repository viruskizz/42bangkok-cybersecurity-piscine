from colorama import Fore, Style
import os

def title(title: str) -> None:
    is_verbose = os.environ.get('INQUISITOR_IS_VERBOSE')
    if eval(is_verbose):
        print(Fore.MAGENTA + title + Style.RESET_ALL)

def info(message: str, key: str = None) -> None:
    is_verbose = os.environ.get('INQUISITOR_IS_VERBOSE')
    if eval(is_verbose):
        if key:
            print(Fore.CYAN + key + Style.RESET_ALL, end=" ")
        print(message)


def error(error: str) -> None:
    is_verbose = os.environ.get('INQUISITOR_IS_VERBOSE')
    if eval(is_verbose):
        print(Fore.RED, end="")
        print(error, end="")
        print(Style.RESET_ALL)
