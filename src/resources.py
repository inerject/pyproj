import os
from pathlib import Path

BASE_DIR_NAME = 'resources'
BASE_DIR_PATH = Path(__file__).parent / BASE_DIR_NAME

FILES = []
DIRECTORIES = []

for entry in os.scandir(path=BASE_DIR_PATH):
    if entry.is_file():
        FILES.append(entry.name)
    if entry.is_dir():
        DIRECTORIES.append(entry.name)


def path(resource_name):
    if not ((resource_name in FILES) or (resource_name in DIRECTORIES)):
        raise ValueError(f'resource "{resource_name}" not found')

    return BASE_DIR_PATH / resource_name
