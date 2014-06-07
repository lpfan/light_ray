import json

from ocr import store_map_path
from base import recognize_text


if __name__ == "__main__":

    with open(store_map_path, 'r') as f:
        store_map = json.load(f)

    raw_check = recognize_text()

    import pdb; pdb.set_trace()  # XXX BREAKPOINT


