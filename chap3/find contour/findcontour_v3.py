import cv2
import numpy as np

img = cv2.imread("/Users/liu/Pictures/pictures for opencv/coins.jpg",cv2.IMREAD_UNCHANGED)
img_downsample = cv2.pyrDown(img)
img_gray = cv2.cvtColor(img_downsample,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
