import os
import sys
import shutil
import argparse
import textwrap

from jschema.load_schemas import loadSchemas
from jschema.errors import JrsError
from jschema.docs import makeDocs

def jschema():
    parser = argparse.ArgumentParser(
        prog="jschema",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
                JsonSchema compiler
            ============================

              1. Read yaml files from --root directory
              2. Resolve $ref in this files
              3. Remove comments keys
              4. Write result to stdout in json format
        """)
    )
    parser.add_argument(
        "-r", "--root",
        dest="root",
        default=str(os.path.abspath(os.getcwd())),
        help="Source directory with schemas (default: %(default)s)"
    )
    parser.add_argument(
        "-p", "--pretty-print",
        dest="prettyPrint",
        action="store_true",
        help="Readable format with indentation"
    )
    args = parser.parse_args()

    schemas = loadSchemas(args.root)
    schemas.initNodes()
    schemas.resolveRefs()
    schemas.clear()

    sys.stdout.write(schemas.toJson(args.prettyPrint))

def jschemaDocs():
    parser = argparse.ArgumentParser(
        prog="jschema-docs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
                JsonSchema Docs generator
            =================================

              1. Read yaml files from --root directory
              2. Resolve $ref in this files
              3. Generate documentation to --destination
        """)
    )
    parser.add_argument(
        "-r", "--root",
        dest="root",
        default=str(os.path.abspath(os.getcwd())),
        help="Source directory with schemas (default: %(default)s)"
    )
    parser.add_argument(
        "-d", "--destination",
        dest="destination",
        required=True,
        help="Output directory for generated documentation"
    )
    parser.add_argument(
        "-f", "--force",
        dest="force",
        action="store_true",
        help="Remove dst directory if exists"
    )
    args = parser.parse_args()

    destinationExists = os.path.exists(args.destination)
    if destinationExists and args.force:
        shutil.rmtree(args.destination, ignore_errors=True)
    elif destinationExists:
        raise JrsError("Destination directory {} exists.\nHINT: Remove directory manyally or add -f (--force) argument".format(
            args.destination
        ))

    os.makedirs(args.destination)

    schemas = loadSchemas(args.root)
    schemas.initNodes()
    schemas.resolveRefs()
    makeDocs(schemas, args.destination)
