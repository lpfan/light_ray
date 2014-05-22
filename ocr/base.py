import Image

from pytesseract import image_to_string
from system import test_image_scan1, test_image_scan2, test_image_scan3


def recognize_text(image_path=test_image_scan1):
    '''Scan image with check, clear it from empty new lines and return as list'''
    text = image_to_string(Image.open(image_path), lang='ukr')
    check = filter(lambda el: el != '', text.split('\n'))
    return check


class BaseHandler(object):
    pass


class BaseStore(object):
    pass
