import os

from test import IMAGE_PATH


test_image_scan1 = os.path.join(IMAGE_PATH, 'scan1.jpg')
test_image_scan2 = os.path.join(IMAGE_PATH, 'scan2.jpg')
test_image_scan3 = os.path.join(IMAGE_PATH, 'scan3.jpg')


store_map_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'map.json'))
