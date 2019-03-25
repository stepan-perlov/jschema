from copy import deepcopy

from .node import Node

class Schema(object):

    def __init__(self, source, sourceDir):
        self.source = deepcopy(source)
        self.dir = sourceDir
        self.id = source["id"]
        self.root = Node(self.id, source, parent=None)
