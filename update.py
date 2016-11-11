"""Test self-update methods."""

import requests

IS_WORKING = True
URL = ''


def download():
    """Download the latest version of this program from GitHub."""
    response = requests.get(URL)
    print(type(response.text))
    print(response.text)


def replace(code):
    """Replace this current program with the given code."""
    pass


def main():
    """Download the latest version and replace this current file with it."""
    download()

if __name__ == '__main__':
    main()
