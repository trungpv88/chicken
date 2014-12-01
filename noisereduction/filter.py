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

class Gabor(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, name="Gabor")
        self._kernel = cv2.getGaborKernel(ksize=(31, 31), sigma=4.0, theta=np.pi/4, lambd=10.0, gamma=0.5, psi=0, ktype=cv2.CV_32F)

    def execute(self, image):
        im_out = cv2.filter2D(image, cv2.CV_8UC3, self._kernel)
        return im_out