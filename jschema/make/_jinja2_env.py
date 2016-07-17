import os
from json import dumps as json_dumps

from jinja2 import Environment, FileSystemLoader

jinja2_env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    trim_blocks=True,
    lstrip_blocks=True,
    extensions=["jinja2.ext.with_"]
)

jinja2_env.filters["type"] = lambda value, expected: type(value) == expected
jinja2_env.filters["intersectionAny"] = lambda arr1, arr2: len(set(arr1).intersection(arr2)) > 0
jinja2_env.filters["intersectionValue"] = lambda arr1, arr2: list(set(arr1).intersection(arr2))[0]
jinja2_env.filters["json_dumps"] = lambda value: json_dumps(value, indent=2, separators=(",", ":"))
