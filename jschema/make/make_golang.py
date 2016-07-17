import io

from _options import Options
from _dump_methods import dump_methods
from _jinja2_env import jinja2_env


def make_golang(schemas, options):
    opts = Options(options)
    template = jinja2_env.get_template("schema_golang.j2")
    data = {"schemas": dump_methods(schemas)}

    with io.open(opts.dst_path, "w", encoding="utf-8") as fstream:
        fstream.write(template.render(data))
