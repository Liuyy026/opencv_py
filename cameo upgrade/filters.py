import cv2
import numpy as np
import utils

#实现图像边缘检测
def strokeEdge (src,dst,blurKsize=7,edgeksize=5):
    if blurKsize>=3:
        blurredSrc = cv2.medianBlur(src,blurKsize)
        graySrc = cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtcolor(src,cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize = edgeksize)
    normalizedInverseAlpha = (1.0/255)*(255-graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel*normalizedInverseAlpha
    cv2.merge(channels,dst)

class VConvolutionFilter(object):
    def __init__(self,kernel):
        self.kernel = kernel
    def apply(self,src,dst):
        cv2.filter2D(src,-1,self._kernel,dst)

class SharpenFilter(VConvolutionFilter):#锐化核
    def __init__ (self):
        kernel = np.array([-1,-1,-1],
                             [-1,9,-1],
                             [-1,-1,-1])
        VConvolutionFilter.__init__(self,kernel)

class FindEdgeFilter(VConvolutionFilter):#边缘检测核
    def __init__(self):
        kernel = np.array([-1,-1,-1],
                          [-1,8,-1],
                          [-1,-1,-1])
        VConvolutionFilter.__init__(self,kernel)

class BlurFilter(VConvolutionFilter):#模糊核
    def __init__(self):
        kernel = np.array([0.4,0.4,0.4,0.4,0.4],
                          [0.4,0.4,0.4,0.4,0.4],
                          [0.4,0.4,0.4,0.4,0.4],
                          [0.4,0.4,0.4,0.4,0.4],
                          [0.4,0.4,0.4,0.4,0.4])
        VConvolutionFilter.__init__(self,kernel)
    
class EmbossFilter(VConvolutionFilter):#一半模糊一半锐化的核
    def __init__(self):
        kernel = np.array([-2,-1,0],
                          [-1,1,-1],
                          [0,1,2])
        VConvolutionFilter.__init__(self,kernel)


