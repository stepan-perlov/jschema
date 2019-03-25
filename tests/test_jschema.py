import os
import sys
import unittest

FILE_DIR = os.path.dirname(__file__)

from jschema import loadSchemas


class TestJschema(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.schemas = loadSchemas(os.path.join(FILE_DIR, "schemas"))
        cls.schemas.initNodes()
        cls.schemas.resolveRefs()

    def testResolveUser(self):
        print(self.schemas.toJson(True))

if __name__ == '__main__':
    unittest.main()
