from colorama import Fore, Style
import os

def log_title(title: str) -> None:
    is_silent = os.environ.get('STOCKHOLM_IS_SILENT')
    if not eval(is_silent):
        print(Fore.LIGHTCYAN_EX + title + Style.RESET_ALL)

def log_info(message: str, key: str = None) -> None:
    is_silent = os.environ.get('STOCKHOLM_IS_SILENT')
    if not eval(is_silent):
        print(key if key else '' + message)