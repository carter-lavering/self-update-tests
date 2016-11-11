"""Test self-update methods."""
import os
import requests

IS_WORKING = True
URL = 'https://raw.githubusercontent.com/carter-lavering/self-update-tests/master/update.py'
PATH = os.path.dirname(os.path.realpath(__file__))


def download():
    """Download the latest version of this program from GitHub."""
    response = requests.get(URL)
    return response.text


def replace_with(code):
    """Replace this current program with the given code."""
    with open('update.py', 'w') as f:
        f.write(code)


def main():
    """Download the latest version and replace this current file with it."""
    replace_with(download())

if __name__ == '__main__':
    main()
