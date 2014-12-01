__author__ = 'User'
import cv2
import numpy as np


class BaseModel(object):
    def __init__(self, name=None):
        self.name = name

    def execute(self):
        raise NotImplementedError("Must implement execute method")

    def test(self):
        im = cv2.imread("NB030.jpg")
        im_out = self.execute(im)
        cv2.imwrite("NB030_out.png", im_out)
        # just for test
        return im_out


class Canny(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, name="Canny")
        self._low_threshold = 100
        self._high_threshold = 200

    def execute(self, image):
        return cv2.Canny(image, self._low_threshold, self._high_threshold)