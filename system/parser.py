import Image

from pytesseract import image_to_string
from system import test_image_scan1, test_image_scan2


def recognize_text(image_path=test_image_scan1):
    text = ''
    text = image_to_string(Image.open(image_path), lang='ukr')
    return text
