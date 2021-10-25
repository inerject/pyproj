import PyInstaller.__main__
from resource import Resource
from pathlib import Path


if __name__ == '__main__':
    args = [
        'pyproj.py',
        '--distpath', str(Path('../dist')),
        '--workpath', str(Path('../build')),
        '--clean',
        '--onefile',
        '--console',
    ]

    for resource in Resource.get_all():
        args.extend(['--add-data', f'{resource};{resource.pyinstaller_dst()}'])

    PyInstaller.__main__.run(args)
