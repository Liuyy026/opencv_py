import cv2
import numpy as np
import utils

def strokeEdge (src,dst,blurKsize=7,edgeksize=5):
    if blurKsize>=3:
        blurredSrc = cv2.medianBlur(src,blurKsize)
        graySrc = cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtcolor(src,cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize = edgeKsize)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel*normalizedInverseAlpha
    cv2.merge(channel,dst)

class VConvolutionFilter(object):
    def __init__(self,kernel):
        self.kernel = kernel
    def apply(self,src,dst):
        cv2.filter2D(src,-1,self._kernel,dst)

class SharpenFilter(VConvolutionFilter):
    def __init__ (self):
        
