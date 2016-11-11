"""Test self-update methods."""
from base64 import b64decode as decode
import requests

__version__ = '1.3.1'
URL = 'http://api.github.com/repos/carter-lavering/self-update-tests/'


def is_outdated():
    """Determine whether the current program is outdated."""
    response = requests.get(URL + 'releases')
    releases = [x['tag_name'][1:] for x in response.json()]
    latest_release = sorted(releases)[-1]
    return __version__ < latest_release


def self_update():
    """Update this script with the latest version from GitHub."""
    response = requests.get(URL + 'contents/update.py')
    encoded = response.json()['content']
    decoded = str(decode(encoded), 'utf-8')
    with open('update.py', 'w') as f:
        f.write(decoded)


def main():
    """Download the latest version and replace this current file with it."""
    if is_outdated():
        print('Updating...', end=' ', flush=True)
        self_update()
        print('Done')
    else:
        print('Latest')

if __name__ == '__main__':
    main()
