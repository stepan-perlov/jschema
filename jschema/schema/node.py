from copy import deepcopy

from .refs_resolver import Ref
from .refs_resolver import RefsResolver


class NodeChilds(object):

    def __init__(self, nodes):
        self.nodes = nodes
        self.isArray = type(nodes) == list
        self.isObject = type(nodes) == dict

    def add(self, child):
        if self.isArray:
            self.node.append(child)
        elif self.isObject:
            self.node[child.key] = child

class Node(object):

    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.parent = parent

        if parent is None:
            self.root = None
            self.path = ""
        elif parent.root is None:
            self.root = parent
            self.path = key
        else:
            self.root = parent.root
            self.path = "{}.{}".format(parent.path, key)

        self.childs = []

    def find(self, path):
        if self.path == path:
            return self

        if self.childs:
            for child in self.childs:
                node = child.find(path)
                if node is not None:
                    return node
        else:
            return None

    def initNodes(self):
        valueType = type(self.value)
        isDict = valueType is dict
        isList = valueType is list

        if isDict and "$ref" in self.value:
            self._resolveRef()
        elif isDict:
            self._resolveDict()
        elif isList:
            self._resolveList()

    def _resolveRef(self):
        print(self.value)
        if self.value["$ref"].index("#") == 0:
            schemaId, path = self.root.key, self.value["$ref"][1:]
        else:
            schemaId, path = self.value["$ref"].split("#")

        path = path.lstrip("/")
        RefsResolver.addRef(Ref(schemaId, path, self))

    def _resolveDict(self):
        for key, value in self.value.items():
            child = Node(key, value, parent=self)
            child.initNodes()
            self.childs.append(child)

    def _resolveList(self):
        for num, value in enumerate(self.value):
            child = Node(num, value, parent=self)
            child.initNodes()
            self.childs.append(child)
