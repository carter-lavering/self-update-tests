"""Test self-update methods."""
from base64 import b64decode as decode
import os
import requests

__version__ = '1.2'
IS_WORKING = True
URL = 'http://api.github.com/repos/carter-lavering/self-update-tests/'
PATH = os.path.dirname(os.path.realpath(__file__))


def get_latest_release():
    """Return this repo's latest release (excluding the "v" at the start)."""
    response = requests.get(URL + 'releases')
    releases = [x['tag_name'][1:] for x in response.json()]
    latest_release = sorted(releases)[-1]
    return latest_release


def outdated():
    """Determine whether the current program is outdated."""
    latest_release = get_latest_release()
    return __version__ < latest_release


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
    if outdated():
        replace_with(download())

if __name__ == '__main__':
    main()
