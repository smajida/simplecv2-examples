#!/usr/bin/python
"""
This program is basically the hello world in SimpleCV
all it does is grab an image from the camera and display it
"""
print __doc__

from simplecv.api import Camera


cam = Camera()

while True:
    img = cam.get_image()
    img.show()
