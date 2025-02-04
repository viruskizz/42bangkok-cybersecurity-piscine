""" Scorpian program """

import sys
import os
import argparse
from PIL import Image, ExifTags
import piexif
from colorama import Fore, Style

EXTENSIONS = [".heif", ".tiff", ".jpg", ".jpeg", ".png", ".gif", ".bmp"]

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Spider", description="scaping image from web")
    parser.add_argument("files", nargs="*")
    parser.add_argument(
        "-d",
        "--delete",
        action='append',
        help="remove metadata EXIF file"
    )
    parser.add_argument(
        "-a",
        "--add",
        action='append',
        help="add metadata EXIF file"
    )
    return parser.parse_args()

def exif_find(tagname):
    """
    Find valid EXIF tags
    read more https://exiftool.org/TagNames/EXIF.html
    """
    all_tags = {
        **{i.value: i.name for i in ExifTags.LightSource},
        **ExifTags.GPSTAGS,
        **ExifTags.TAGS
    }
    for code,name in all_tags.items():
        if tagname == name:
            return code

def exif_display(fname):
    """ Display EXIF data """
    img = Image.open(fname)
    img_exif = img.getexif()
    if not img_exif:
        print(Fore.MAGENTA + 'NO EXIF DATA' + Style.RESET_ALL)
        return
    for key, val in img_exif.items():
        if key in ExifTags.TAGS:
            print(f'{ExifTags.TAGS[key]}:\t{val}')

def exif_add(fname, adds):
    im = Image.open(fname)
    exif_data = im.getexif()
    for add in adds:
        key,value = add.split("=")
        code = exif_find(key)
        if code:
            exif_data[code] = value
    im.convert('RGB').save('test.jpg', 'JPEG', exif=exif_data)

def validate(fname: str):
    """ Validate EXIF file """
    ext = os.path.splitext(fname)[1]
    if ext not in EXTENSIONS:
        print(Fore.RED + "INVALID_FILE_EXTENSION" + Style.RESET_ALL)
        return False
    return True

if __name__ == '__main__':
    n = len(sys.argv)
    args = optparsing()
    print('args:', args)
    for filename in args.files:
        print(Fore.CYAN + f'File: {filename}' + Style.RESET_ALL)
        if not validate(filename):
            continue
        exif_display(filename)
        if args.add and len(args.add) > 0:
            exif_add(filename, args.add)
