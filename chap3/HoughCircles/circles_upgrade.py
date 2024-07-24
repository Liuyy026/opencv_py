import cv2
import numpy as np

# 读取图像
img = cv2.imread('/Users/liu/Pictures/pictures for opencv/planets.jpg')

# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 中值滤波
gray_img = cv2.medianBlur(gray_img, 5)

# 使用霍夫圆检测
circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# 检查是否检测到圆形
if circles is not None:
    circles = np.uint16(np.around(circles))

    # 在原图像上绘制检测到的圆形
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 外圆
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)     # 圆心

# 使用自适应阈值以更好地分离背景和前景
thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 2)

# 检测轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制检测到的轮廓
cv2.drawContours(img, contours, -1, (125, 0, 125), 2)

# 显示处理后的图像
cv2.imshow("Circles and Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存处理后的图像
cv2.imwrite("/Users/liu/code/opencv_py/chap3/HoughCircles/planets_circles_contours.jpg", img)