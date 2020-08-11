import cv2
import glob
import numpy as np
from numpy import random

path = "videooutput/*.jpg"

for bb,file in enumerate (glob.glob(path)):
    a = cv2.imread(file)
    blur = cv2.GaussianBlur(a, (5, 5), 3)
    #blur =  cv2.blur(a,(11,11))
    cv2.imwrite('./gaussianvideo/{}.jpg'.format(bb), blur)
    cv2.waitKey(20)


