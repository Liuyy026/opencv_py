import cv2
import numpy as np

img = cv2.imread("/Users/liu/Pictures/pictures for opencv/lmw.jpg",0)
cv2.imwrite("/Users/liu/code/opencv_py/canny/Canny.jpg",cv2.Canny(img,200,300))
cv2.imshow("Canny",cv2.imread("Canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows
