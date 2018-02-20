.. jschema documentation master file, created by
   sphinx-quickstart on Wed Jul 13 18:52:39 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

jschema
=======

.. code-block:: python

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

.. code-block:: bash

$ jschema --root /root/schemas/folder > result.json
$ jschema-docs --root /root/schemas/folder --destination /root/docs/folder

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
