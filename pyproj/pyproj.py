import os
import argparse
import files_from_tmpl
import resources
import subprocess


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'proj_name')
    parser.add_argument(
        '-t', '--template', default=resources.path('template'))
    parser.add_argument(
        '-v', '--py_ver', default='')

    args = parser.parse_args()

    #
    files_from_tmpl.generate(
        src=args.template,
        dst_name=args.proj_name,
        rewrite=True,
    )

    #
    if args.py_ver:
        if not args.py_ver.startswith('-'):
            args.py_ver = '-' + args.py_ver

    run_ps_script_cmd = 'powershell {ps_script_path} {ps_script_args}'.format(
        ps_script_path=resources.path('venv.ps1'),
        ps_script_args=f'-py_ver "{args.py_ver}"',
    )

    os.chdir(args.proj_name)
    subprocess.Popen(run_ps_script_cmd.split(), shell=True).wait()
