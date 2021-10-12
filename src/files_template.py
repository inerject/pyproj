from pathlib import Path
import os
import shutil
import jinja2


def replicate(*, src='./template', dst='./output', rewrite=False, **kwargs):
    src = Path(src)
    if not src.is_dir():
        raise ValueError('"src" must be a directory')

    dst = Path(dst)
    if rewrite and dst.is_dir():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    kwargs['replica_name'] = dst.name

    #
    def process_dir(proc_src: Path):
        base_src_relative = proc_src.relative_to(src)
        proc_dst_relative = f'{base_src_relative}'.format(**kwargs)
        proc_dst = dst.joinpath(proc_dst_relative)
        if not proc_dst.exists():
            os.mkdir(proc_dst)

        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(proc_src),
            keep_trailing_newline=True,
        )

        for proc_src_entry in os.scandir(path=proc_src):
            if proc_src_entry.is_dir():
                process_dir(Path(proc_src_entry.path))

            elif proc_src_entry.is_file():
                is_tmpl_file = proc_src_entry.name.endswith('.tmpl')

                output_file_name = proc_src_entry.name
                if is_tmpl_file:
                    output_file_name = output_file_name.replace('.tmpl', '')
                output_file_name = output_file_name.format(**kwargs)
                output_file_path = proc_dst.joinpath(output_file_name)

                if is_tmpl_file:
                    template = env.get_template(proc_src_entry.name)
                    with open(output_file_path, 'w') as f:
                        f.write(template.render(kwargs))
                else:
                    shutil.copy(proc_src_entry.path, output_file_path)

    #
    process_dir(src)
