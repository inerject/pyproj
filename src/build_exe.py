import PyInstaller.__main__


PyInstaller.__main__.run([
    'pyproj.py',
    '--distpath', '../dist',
    '--workpath', '../build',
    '--add-data', 'resources/template;resources/template',
    '--add-data', 'resources/venv.ps1;resources/.',
    '--clean',
    '--onefile',
    '--console',
])
