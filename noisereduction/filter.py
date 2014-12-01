__author__ = 'User'
import cv2
import numpy as np


class BaseModel(object):
    def __init__(self, name=None):
        self.name = name

    def execute(self):
        raise NotImplementedError("Must implement execution method")


class Median(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, "Mean")
        self._ksize = 5

    def execute(self, image):
        im_out = cv2.medianBlur(image, self._ksize)
        return im_out