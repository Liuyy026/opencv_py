import cv2
import numpy as np

img = cv2.imread("/Users/liu/Pictures/图像识别图片素材/lmw.jpg",0)
cv2.imwrite("Canny.jpg",cv2.Canny(img,200,300))
cv2.imshow("Canny",cv2.imread("Canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows
