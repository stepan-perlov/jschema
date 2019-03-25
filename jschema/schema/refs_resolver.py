from copy import deepcopy

from jschema.errors import JrsNodeError
from jschema.errors import JrsRefNotFound
from jschema.errors import JrsNoSchemaWithoutRefs
from jschema.errors import JrsCircularRefs

class RefsGroup(object):

    def __init__(self, name):
        self._name = name
        self._group = {}
        self._cachedPathes = {}

    def add(self, schemaId, path, ref):
        if schemaId not in self._group:
            self._group[schemaId] = {}

        self._group[schemaId][path] = ref

    def getPathes(self, schemaId):
        if schemaId not in self._cachedPathes:
            self._cachedPathes[schemaId] = reversed(sorted(
                self._group[schemaId].keys()
            ))
        return self._cachedPathes[schemaId]

    def getRef(self, schemaId, path):
        return self._group[schemaId][path]


class Ref(object):

    def __init__(self, schemaId, path, targetNode):
        self.schemaId = schemaId
        self.path = path
        self.target = targetNode
        self.refNode = None
        self.resolved = False


class RefsResolver(object):
    _schemas = {}
    _targets = RefsGroup("targets")
    _refs = []

    @classmethod
    def addSchema(cls, schema):
        cls._schemas[schema.id] = schema

    @classmethod
    def addRef(cls, ref):
        if ref.schemaId not in cls._schemas:
            raise JrsNodeError(JrsNodeError.make_message("Schema '{}' not exists".format(ref.schemaId), ref.target))

        cls._targets.add(
            schemaId=ref.target.root.key,
            path=ref.target.path,
            ref=ref
        )
        cls._refs.append(ref)

    @classmethod
    def _resolveRefs(cls, ref, fromRefs):
        if ref.resolved:
            return

        if ref.refNode is None:
            ref.refNode = cls._schemas[ref.schemaId].root.find(ref.path)
            if ref.refNode is None:
                raise JrsRefNotFound("Ref not found, schemaId: {}, path: {}".format(ref.schemaId, ref.path))

        relatedRef = None
        for path in cls._targets.getPathes(ref.schemaId):
            if path.startswith(ref.target.path):
                relatedRef = cls._targets.getRef(ref.schemaId, path)
                break;

        if relatedRef in fromRefs:
            raise JrsCircularRefsException("")

        if relatedRef is None:
            ref.target.parent.value[ref.target.key] = ref.refNode.value
            ref.resolved = True
        elif relatedRef in fromRefs:
            raise JrsCircularRefs(JrsCircularRefs.make_message([relatedRef, ref] + fromRefs))
        else:
            if relatedRef.refNode is None:
                relatedRef.refNode = cls._schemas[relatedRef.schemaId].root.find(relatedRef.path)
                if relatedRef.refNode is None:
                    raise JrsRefNotFound("Ref not found, schemaId: {}, path: {}".format(relatedRef.schemaId, relatedRef.path))

            cls._resolveRefs(relatedRef, [ref] + fromRefs)
            ref.target.parent.value[ref.target.key] = ref.refNode.value
            ref.resolved = True

    @classmethod
    def resolveRefs(cls):
        for ref in cls._refs:
            cls._resolveRefs(ref, fromRefs=[])
