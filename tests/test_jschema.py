import os
import sys
import unittest
FILE_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(FILE_DIR, ".."))

from jschema import Schema


class TestJschema(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.schema = Schema(os.path.join(FILE_DIR, "schemas"))
        cls.schema.load()

    def test_resolve_refs(self):
        self.schema.resolve_refs()
        self.assertEqual(
            self.schema._schemas["user"]["properties"],
            self.schema._schemas["user"]["resolvedProperties"]
        )

if __name__ == '__main__':
    unittest.main()
