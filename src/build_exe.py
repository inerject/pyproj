import PyInstaller.__main__
import resources
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

    def add_data_arg(item, *, is_dir):
        src = resources.BASE_DIR_PATH / item
        if is_dir:
            dst = Path(resources.BASE_DIR_NAME) / item
        else:
            dst = Path(resources.BASE_DIR_NAME) / '.'
        args.extend(['--add-data', f'{src};{dst}'])

    for item in resources.FILES:
        add_data_arg(item, is_dir=False)
    for item in resources.DIRECTORIES:
        add_data_arg(item, is_dir=True)

    PyInstaller.__main__.run(args)
