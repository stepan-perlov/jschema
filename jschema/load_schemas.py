import os
import json
import yaml
import subprocess

from .errors import JrsSchemaError
from .schema import Schema
from .schema import RefsResolver


class Schemas(list):

    def initNodes(self):
        for item in self:
            item.root.initNodes()

    def resolveRefs(self):
        RefsResolver.resolveRefs()

    def clear(self):
        for item in self:
            item.root.clear()

    def toJson(self, prettyPrint):
        schemas = {}
        for item in self:
            schemas[item.id] = item.root.value

        if prettyPrint:
            return json.dumps(schemas, separators=(',', ': '), indent=4)
        else:
            return json.dumps(schemas, separators=(',', ':'))


def loadSchemas(rootDir):
    schemas = Schemas()

    res = subprocess.check_output(["find", rootDir, "-name", "*.yaml"])
    for fpath in res.split():
        print(fpath)
        with open(fpath) as fstream:
            source = yaml.load(fstream)

        if "id" not in source:
            raise JrsSchemaError("Attribute 'id' not exists: {}".format(fpath))
        if "type" not in source:
            raise JrsSchemaError("Attribute 'type' not exists: {}".format(fpath))
        if source["type"] == "method" and "params" not in source:
            raise JrsSchemaError("Attribute 'params' not exists in method: {}".format(fpath))

        sourceDir = os.path.dirname(fpath).decode("utf-8").replace(rootDir, "", 1).lstrip("/")

        schema = Schema(source, sourceDir)
        RefsResolver.addSchema(schema)
        schemas.append(schema)

    return schemas
