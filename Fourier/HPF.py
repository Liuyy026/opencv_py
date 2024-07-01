import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([[-1,-1,-1],
                        [-1,-8,-1],
                        [-1,-1,-1]]
                  )

kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                       [-1,1,2,1,-1],
                       [-1,2,4,2,-1],
                       [-1,1,2,1,-1],
                       [-1,-1,-1,-1,-1]]
)

img = cv2.imread("/Users/liu/Pictures/图像识别图片素材/lmw.jpg",0)
k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernel_5x5)

blurred = cv2.GaussianBlur(img,(17,17),0)
g_hpf = img - blurred

cv2.imwrite("/Users/liu/code/opencv_py/Fourier/3x3.png",k3)
cv2.imwrite("/Users/liu/code/opencv_py/Fourier/5x5.png",k5)
cv2.imwrite("/Users/liu/code/opencv_py/Fourier/blurred.png",blurred)
cv2.imwrite("/Users/liu/code/opencv_py/Fourier/hpf.png",g_hpf)

cv2.imshow("3x3",k3)
cv2.imshow("5x5",k5)
cv2.imshow("blurred",blurred)
cv2.imshow("hpf",g_hpf)
cv2.waitKey(0)
cv2.destroyAllWindows

