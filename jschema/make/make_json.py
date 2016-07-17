import os
import io

from _options import Options
from _dump_methods import dump_methods


def make_json(schemas, options):
    opts = Options(options)
    formated = dump_methods(schemas)
    for key, sch in formated:
        fpath = os.path.join(opts.dst_dir, key)
        with io.open(fpath, "w", encoding="utf-8") as fstream:
            fstream.write(sch)
