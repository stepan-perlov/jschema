import os
import shutil
from jschema import Schema

FILE_DIR = os.path.dirname(__file__)
BUILD_DIR = os.path.join(FILE_DIR, "build")
PLAIN_SCHEMA_DIR = os.path.join(FILE_DIR, "plain_schema")
STRUCTED_SCHEMA_DIR = os.path.join(FILE_DIR, "structed_schema")

shutil.rmtree(BUILD_DIR)
os.makedirs(BUILD_DIR)



# plain schema
schema = Schema()

schema.load(PLAIN_SCHEMA_DIR)
schema.resolve_refs()
schema.clear()

schema.format("golang", {"dst": BUILD_DIR, "ns": "build"})
schema.format("ajv", {"dst": BUILD_DIR, "ns": None})
schema.format("json", {"dst": BUILD_DIR, "ns": None})



# structed schema
schema = Schema()

schema.load(STRUCTED_SCHEMA_DIR)
schema.resolve_refs()
schema.clear()

schema.format("golang", {"dst": BUILD_DIR, "ns": "build"})
schema.format("ajv", {"dst": BUILD_DIR, "ns": None})
schema.format("json", {"dst": BUILD_DIR, "ns": None})
