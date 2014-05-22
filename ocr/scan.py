import json

from handlers import store_map_path


if __name__ == "__main__":
    store_map = json.load(open(store_map_path, 'r'))
    import pdb; pdb.set_trace()  # XXX BREAKPOINT


