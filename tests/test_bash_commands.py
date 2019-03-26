import os
import subprocess
import unittest

from jschema import loadSchemas

FILE_DIR = os.path.dirname(__file__)
MUTLIREFS_ROOT = os.path.join(FILE_DIR, "sources", "multirefs")


class TestBashCommands(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(FILE_DIR, "results", "cleared_mutirefs.json")) as fstream:
            cls.clearedExpected = fstream.read()

        with open(os.path.join(FILE_DIR, "results", "not_cleared_mutirefs.json")) as fstream:
            cls.notClearedExpected = fstream.read()

    def testJschemaMultirefs(self):
        res = subprocess.check_output("jschema --root {} --prettyPrint".format(MUTLIREFS_ROOT), shell=True)
        self.assertEqual(res.decode(), self.clearedExpected)

    def testJschemaDocsMultirefs(self):
        res = subprocess.check_output("jschema-docs --force --root {} --destination {}".format(
            MUTLIREFS_ROOT,
            os.path.join(FILE_DIR, "build")
        ), shell=True)

if __name__ == '__main__':
    unittest.main()
