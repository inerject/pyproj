import os
import argparse
import files_template
from pathlib import Path
import subprocess


def resource_path(relative_path):
    return Path(__file__).parent / 'resources' / relative_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proj_name')
    parser.add_argument(
        '--template', default=resource_path('template'))

    args = parser.parse_args()

    #
    files_template.replicate(
        dst=args.proj_name,
        src=args.template,
        rewrite=True,
    )

    #
    os.chdir(args.proj_name)
    run_ps_script_cmd = 'powershell {ps_script_path}'.format(
        ps_script_path=resource_path('venv.ps1'))
    subprocess.Popen(run_ps_script_cmd.split(), shell=True).wait()
