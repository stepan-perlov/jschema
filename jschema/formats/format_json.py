# -*- coding: utf-8 -*-
import os
import json

from ._options import Options
from ._dump_methods import dump_methods


def format_json(schema, options):
    opts = Options(options)
    formated = dump_methods(schema)
    for ns in formated:
        for method, sch in formated[ns].iteritems():
            fpath = os.path.join(opts.dst_dir, u"{}.{}.json".format(ns, method))
            with open(fpath, "w") as fstream:
                fstream.write(json.dumps(sch, indent=2, separators=(",", ": ")) + "\n")
