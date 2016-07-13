.. jschema documentation master file, created by
   sphinx-quickstart on Wed Jul 13 18:52:39 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

jschema
=======

.. code-block:: python

    >>> from jschema import Schema
    >>> schema = Schema("/root/schemas/folder")

    >>> # load all *.yaml file in directory "/root/schemas/folder"
    >>> schema.load()
    >>> # replace $ref with reference
    >>> schema.resolve_refs()

    >>> # make docs
    >>> schema.make("docs", "/build/root/docs")

    >>> # remove title and description attributes
    >>> schema.clear()
    >>> # make another format from schemas
    >>> schema.make("json", "/build/root/json")
    >>> schema.make("js", "/build/path/to/file.js")

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
