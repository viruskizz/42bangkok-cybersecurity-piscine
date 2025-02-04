"""
Spider program
"""

import os
import argparse
import requests
from bs4 import BeautifulSoup


SEARCHED = []
EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Spider", description="scaping image from web")
    parser.add_argument("urls", nargs="*")
    parser.add_argument(
        "-r",
        "--recursive",
        default=False,
        action="store_true",
        help="recursively downloads the images in a URL received as a parameter"
    )
    parser.add_argument(
        "-l",
        "--level",
        type=int,
        default=5,
        help="indicates the maximum depth level of the recursive download, default is 5"
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default="./data/",
        help="The path where the downloaded files will be saved, default is ./data/"
    )
    return parser.parse_args()

def save_file(filename, content):
    """Save content to file"""
    with open(filename, "wb") as file:
        file.write(content)

def save_all_images(curl: str, soup: BeautifulSoup, arg):
    """ Save all img to file """
    for img in soup.find_all('img'):
        link = img.get('src')
        ext = os.path.splitext(link)[1]
        filename = os.path.join(arg.path, os.path.basename(link))
        if ext not in EXTENSIONS:
            continue
        if link.startswith("/"):
            link = curl + link
        r = requests.get(link, timeout=3, stream=True)
        save_file(filename, r.content)
        print(f'Saved: {filename}')

def navigate(curl: str, arg, times=0):
    """Navigate to url"""
    print(f"URL[{times}]: {curl}")
    r = requests.get(curl, timeout=3)
    times += 1
    SEARCHED.append(curl)
    if r.status_code == 200:
        html_doc = r.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        if arg.recursive and times < arg.level:
            for a in soup.find_all('a'):
                link = a.get('href')
                if link.startswith('#') or link.startswith('?'):
                    continue
                if link.startswith("/"):
                    link = curl + link
                if link not in SEARCHED:
                    navigate(link, arg, times)
        save_all_images(curl, soup, arg)

if __name__ == '__main__':
    args = optparsing()
    print('args:', args)
    if not os.path.exists(args.path):
        os.makedirs(args.path)
    for url in args.urls:
        navigate(url, args)
