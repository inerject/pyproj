import os
import argparse
import files_template
import resources
import subprocess


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proj_name')
    parser.add_argument(
        '--template', default=resources.path('template'))

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
        ps_script_path=resources.path('venv.ps1'))
    subprocess.Popen(run_ps_script_cmd.split(), shell=True).wait()
