import os
import unittest

from jschema import loadSchemas
from jschema.errors import JrsSchemaError
from jschema.errors import JrsSchemaNotFound
from jschema.errors import JrsNodeNotFound
from jschema.errors import JrsCircularRefs

FILE_DIR = os.path.dirname(__file__)
MUTLIREFS_ROOT = os.path.join(FILE_DIR, "sources", "multirefs")
SCHEMA_ERROR_ROOT = os.path.join(FILE_DIR, "sources", "schema_error")
SCHEMA_NOT_FOUND_ROOT = os.path.join(FILE_DIR, "sources", "schema_not_found")
NODE_NOT_FOUND_ROOT = os.path.join(FILE_DIR, "sources", "node_not_found")
CIRCULAR_ROOT = os.path.join(FILE_DIR, "sources", "circular")

class TestPythonLogic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(FILE_DIR, "results", "cleared_mutirefs.json")) as fstream:
            cls.clearedExpected = fstream.read()

        with open(os.path.join(FILE_DIR, "results", "not_cleared_mutirefs.json")) as fstream:
            cls.notClearedExpected = fstream.read()

    def testClearedMultirefs(self):
        ctx = loadSchemas(MUTLIREFS_ROOT)
        ctx.initNodes(clear=True)
        ctx.resolveRefs()

        self.assertEqual(ctx.toJson(prettyPrint=True), self.clearedExpected)

    def testNotClearedMultirefs(self):
        ctx = loadSchemas(MUTLIREFS_ROOT)
        ctx.initNodes(clear=False)
        ctx.resolveRefs()

        self.assertEqual(ctx.toJson(prettyPrint=True), self.notClearedExpected)

    def testSchemaError(self):
        self.assertRaisesRegex(
            JrsSchemaError,
            "Attribute 'id' not exists:.*sources/schema_error/user.yaml",
            loadSchemas,
            SCHEMA_ERROR_ROOT
        )

    def testSchemaNotFound(self):
        ctx = loadSchemas(SCHEMA_NOT_FOUND_ROOT)
        self.assertRaisesRegex(
            JrsSchemaNotFound,
            "Schema not found, schemaId: typesMistake",
            ctx.initNodes
        )

    def testNodeNotFound(self):
        ctx = loadSchemas(NODE_NOT_FOUND_ROOT)
        ctx.initNodes()
        self.assertRaisesRegex(
            JrsNodeNotFound,
            "Not found node with schemaId: types, path: date_range_mistake",
            ctx.resolveRefs
        )

    def testCircularException(self):
        ctx = loadSchemas(CIRCULAR_ROOT)
        ctx.initNodes()
        self.assertRaisesRegex(
            JrsCircularRefs,
            "Circular references: chicken#struct -> egg#struct -> chicken#struct",
            ctx.resolveRefs
        )


if __name__ == '__main__':
    unittest.main()
