"""Test self-update methods."""
from base64 import b64decode as decode
import os
import requests

VERSION = 'v1.1'
IS_WORKING = True
URL = 'http://api.github.com/repos/carter-lavering/self-update-tests/'
PATH = os.path.dirname(os.path.realpath(__file__))


def releases():
    """Return this repo's releases."""
    response = requests.get(URL + 'releases')
    return [x['tag_name'] for x in response.json()]


def download():
    """Return the latest version of this program from GitHub."""
    response = requests.get(URL + 'contents/update.py')
    encoded = response.json()['content']
    decoded = str(decode(encoded), 'utf-8')
    return decoded


def replace_with(code):
    """Replace this current program with the given code."""
    with open('update.py', 'w') as f:
        f.write(code)


def main():
    """Download the latest version and replace this current file with it."""
    replace_with(download())
    print(download())
    # print('\n'.join(releases()))

if __name__ == '__main__':
    main()
