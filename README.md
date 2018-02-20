# jschema

## Json Schema compiler

1. Read yaml files from --root directory
2. Resolve $ref in this files
3. Remove comments keys
4. Write result to stdout in json format

**Usage in python3:**
```python3

    >>> from jschema import Schema
    >>> schema = Schema()

    >>> # load all *.yaml file in directory "/root/schemas/folder"
    >>> schema.load("/root/schemas/folder")
    >>> # replace $ref with reference
    >>> schema.resolve_refs()
    >>> # remove title and description attributes
    >>> schema.clear()
    >>> # dumps resolved schemas
    >>> schema.toJson()

```

**Usage in bash:**
```bash

$ jschema --root /root/schemas/folder > result.json

```

## JsonSchema Docs generator

1. Read yaml files from --root directory
2. Resolve $ref in this files
3. Generate documentation to --destination

**Usage:**
```bash

$ jschema-docs --root /root/schemas/folder --destination /root/docs/folder

```
