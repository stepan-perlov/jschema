import os
import json
import shutil
from jinja2 import Environment, FileSystemLoader

curDir = os.path.abspath(os.path.dirname(__file__))

def makeDocs(schema, dstDir):
    jinjaEnv = Environment(
        loader=FileSystemLoader(os.path.join(curDir, "templates")),
        trim_blocks=True,
        lstrip_blocks=True,
        extensions=["jinja2.ext.with_"]
    )
    jinjaEnv.filters["jsonPrettyDump"] = lambda value: json.dumps(value, separators=(',', ': '), indent=4)
    schemasDir = os.path.join(dstDir, "schemas")
    if not os.path.exists(schemasDir):
        os.mkdir(schemasDir)

    vendorDir = os.path.join(dstDir, "vendor")
    if not os.path.exists(vendorDir):
        shutil.copytree(os.path.join(curDir, "vendor"), vendorDir)

    indexTemplate = jinjaEnv.get_template("index.j2")

    methods = []
    definitions = []
    for item in schemas:
        if item["type"] == "method":
            methods.append(item.id)
        elif item["type"] == "definitions":
            definitions.append(item.id)
    indexPath = os.path.join(dstDir, "index.html")
    with open(indexPath, "w") as fstream:
        fstream.write(indexTemplate.render(methods=sorted(methods), definitions=sorted(definitions)))
    print(" - Created: " + indexPath)

    schemaTemplate = jinjaEnv.get_template("schema.j2")
    for item in schemas:
        schemaPath = os.path.join(schemasDir, item.id + ".html")
        with open(schemaPath, "w") as fstream:
            fstream.write(schemaTemplate.render(schema=item.root.value))
        print(" - Created: " + schemaPath)
