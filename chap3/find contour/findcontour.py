import cv2
import numpy as np

img = np.zeros((200,200),dtype = np.uint8)
img[50:150,50:150] = 255

ret,tresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                                        #RETER_TREE 函数检测内部轮廓和外部轮廓
color = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color,contours,-1,(125,0,125),2)
cv2.imshow("contours",color)
cv2.waitKey()
cv2.destroyAllWindows()