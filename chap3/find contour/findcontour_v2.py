import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread("/Users/liu/Pictures/pictures for opencv/mty_demo1.jpg",cv2.IMREAD_UNCHANGED))

ret,thresh = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),127,255,cv2.THRESH_BINARY)
contours,hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #find minium area
    rect =cv2.minAreaRect(c)
    #calculate coordinate of minium area rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    #draw contour
    cv2.drawContours(img,[box],0,(0,255,0),3)

    #calculate center and radius of minium enclosing circle
    (x,y),radius = cv2.minEnclosingCircle(c)
    #cast to integers
    center =(int(x),int(y))
    radius =int(radius)
    #draw a circle
    img = cv2.circle(img,center,radius,(0,255,0),2)

    cv2.drawContours(img,contours,-1,(255,0,0),1)
    cv2.imshow("contours",img)

    cv2.waitKey()
    cv2.destroyAllWindows()