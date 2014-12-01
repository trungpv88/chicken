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


class Sobel(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, name="Sobel")
        self._ksize = 5

    def execute(self, image):
        # gradient X
        sobel_x = cv2.Sobel(image, cv2.CV_8U, 1, 0, self._ksize)
        # gradient Y
        sobel_y = cv2.Sobel(image, cv2.CV_8U, 0, 1, self._ksize)
        sobel = None
        # sobel = sqrt(sobel_x * sobel_x + sobel_y * sobel_y)
        sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
        return sobel


class Laplacian(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, name="Laplace")

    def execute(self, image):
        return cv2.Laplacian(image, cv2.CV_8U)
