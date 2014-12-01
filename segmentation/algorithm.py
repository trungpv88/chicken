__author__ = 'User'
import cv2
import numpy as np


class BaseModel(object):
    def __init__(self, name=None):
        self.name = name

    def execute(self):
        raise NotImplementedError("Must implement execute method")

    def test(self, image):
        im = cv2.imread("NB030.jpg")
        im_out = self.execute(im)
        cv2.imwrite("NB030_out.png", im_out)
        return im_out


class KMeans(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, name="Kmeans")
        self._criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        self._num_cluster = 4

    def execute(self, image):
        Z = image.reshape((-1, 3))
        Z = np.float32(Z)
        ret, label, center = cv2.kmeans(Z, self._num_cluster, None, self._criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape(image.shape)
        return res2


class Canny(BaseModel):
    def __init__(self):
        BaseModel.__init__(self, name="Canny")
        self._low_threshold = 100
        self._high_threshold = 200

    def execute(self, image):
        return cv2.Canny(image, self._low_threshold, self._high_threshold)