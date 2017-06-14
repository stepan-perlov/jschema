# -*- coding: utf-8 -*-
import os

from jschema.make._options import Options
from jschema.make._dump_methods import dump_methods
from jschema.make._jinja2_env import jinja2_env


def make_ajv(schema, options):
    opts = Options(options)
    template = jinja2_env.get_template("schema_ajv.j2")

    for key, sch in schema.schemas.iteritems():
        if sch["type"] != "method":
            continue

        dst_dir = os.path.join(opts.dst_dir, schema.schemas_dirs[key])
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        name = key.replace(".", "_")

        file_path = "{}/{}.js".format(dst_dir, name)
        with open(file_path, "w") as fstream:
            fstream.write(template.render({
                "schema": sch
            }))
        print(" - Created: {}".format(file_path))
