import os
import shutil
from jschema import Schema

FILE_DIR = os.path.dirname(__file__)
BUILD_DIR = os.path.join(FILE_DIR, "build")
SCHEMA_DIR = os.path.join(FILE_DIR, "schema")

shutil.rmtree(BUILD_DIR)
os.makedirs(BUILD_DIR)

schema = Schema()

schema.load(SCHEMA_DIR)
schema.resolve_refs()
schema.clear()

schema.make("golang", {"dst_dir": BUILD_DIR, "ns": "build"})
schema.make("ajv", {"dst_path": os.path.join(BUILD_DIR, "schema-ajv.js")})
schema.make("json", {"dst_dir": BUILD_DIR})
