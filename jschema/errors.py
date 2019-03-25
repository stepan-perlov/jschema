import json


class JrsError(Exception):
    pass


class JrsRefNotFound(JrsError):
    pass


class JrsSchemaError(JrsError):
    pass


class JrsNodeError(JrsError):
    @staticmethod
    def make_message(message, node):
        return "{}. node: {}, schema_id: {}".format(
            message,
            json.dumps(node.parent.value, indent=2, separators=(',', ': ')),
            node.rootNode.key
        )

class JrsFormatingError(JrsError):
    pass

class JrsNoSchemaWithoutRefs(JrsError):
    pass

class JrsCircularRefs(JrsError):
    @staticmethod
    def make_message(relatedRefs, fromRefs):
        return "Circular references: {}".format(
            " -> ".join([
                "{}#{}".format(ref.rootId, ref.path)
                for ref in reversed(fromRefs)
            ])
        )
