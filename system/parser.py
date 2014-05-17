import Image
import os

from pytesseract import image_to_string

from test import IMAGE_PATH


test_image_scan1 = os.path.join(IMAGE_PATH, 'scan1.jpg')
test_image_scan2 = os.path.join(IMAGE_PATH, 'scan2.jpg')

def recognize_text(image_path=test_image_scan1):
    text = ''
    text = image_to_string(Image.open(image_path), lang='ukr')
    return text
