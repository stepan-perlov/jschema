# -*- coding: utf-8 -*-
import io
import subprocess

import yaml

from node import RootNode
from errors import JrsSchemaError
import make


class Schema(object):

    def __init__(self):
        self._schemas = {}
        self._nodes = {}

    @property
    def schemas(self):
        return self._schemas

    def load(self, root):
        res = subprocess.check_output(["find", root, "-name", "*.yaml"])
        for fpath in res.split():
            with io.open(fpath, encoding="utf-8") as fstream:
                schema = yaml.load(fstream)

            if "id" not in schema:
                raise JrsSchemaError(u"Attribute 'id' not exists: {}".format(fpath))
            if "type" not in schema:
                raise JrsSchemaError(u"Attribute 'type' not exists: {}".format(fpath))
            if schema["type"] == "method" and "params" not in schema:
                raise JrsSchemaError(u"Attribute 'params' not exists in method: {}".format(fpath))

            self._schemas[schema["id"]] = schema

    def resolve_refs(self):
        RootNode.set_schemas(self._schemas)
        for key in self._schemas:
            schema_node = RootNode(key)
            schema_node.find_refs()
            schema_node.replace_refs()
            self._nodes[key] = schema_node

    def clear(self):
        for schema in self._schemas.values():
            RootNode.clear(schema)

    def make(self, make_format, options):
        make_proc = getattr(make, make_format, None)
        if make_proc is None:
            raise JrsSchemaError("Unexpected make format '{}'".format(make_format))
        else:
            make_proc(self, options)
