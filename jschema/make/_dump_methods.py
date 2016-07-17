

def dump_methods(schemas):
    tree = {}
    for key, sch in schemas.iteritems():
        if sch["type"] == "method":
            ns, method = key.split(".")
            if ns not in tree:
                tree[ns] = {}
            tree[ns][method] = {}
            tree[ns][method] = sch

    return tree
