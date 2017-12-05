# -*- coding: utf-8 -*-
import os

class Options(object):

    def __init__(self, options):
        self._dst_dir = options["dst_dir"]
        self._ns = options["ns"]

    @property
    def dst_dir(self):
        return self._dst_dir

    @property
    def ns(self):
        return self._ns
