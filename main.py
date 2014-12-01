#!/usr/bin/env python

'''
Image processing with opencv in Python.

Keys:
    ESC    - exit
    SPACE  - display images captured from camera
    k      - apply k-means algorithm for segmentation
    c      - apply canny algorithm for edge detection
'''

__author__ = 'User'
import cv2
from segmentation.algorithm import KMeans, Canny


class Camera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self._quit = False
        self._k_means = None
        self._canny = None
        self._frame = None
        self._normal = True

    def run(self):
        while True:
            key_code = cv2.waitKey(20) # delay 20ms
            self.on_key_press(key_code)
            ret, frame = self.cap.read()
            if self._quit:
                break
            elif self._k_means is not None:
                self._frame = self._k_means.execute(frame)
                # self._frame = self._k_means.test(frame)
            elif self._canny is not None:
                self._frame = self._canny.execute(frame)
                # self._frame = self._canny.test(frame)
            elif self._normal:
                self._frame = frame
            cv2.imshow('Chicken', self._frame)
        self.cap.release()
        cv2.destroyAllWindows()

    def on_key_press(self, key_code):
        if key_code == 27:
            self._quit = True
        elif key_code == 107:
            self.reset_operator()
            self._k_means = KMeans()
        elif key_code == 99:
            self.reset_operator()
            self._canny = Canny()
        elif key_code == 32:
            self.reset_operator()
            self._normal = True

    def reset_operator(self):
        self._k_means = None
        self._canny = None
        self._normal = False

if __name__ == "__main__":
    print __doc__
    Camera().run()