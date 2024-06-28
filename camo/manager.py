import cv2
import numpy as np
import time

class CaptureManager:
    def __init__(self, capture, previewWindowManager=None, shouldMirrorPreview=False, shouldFlipPreview=False):
        self._capture = capture
        self.previewWindowManager = previewWindowManager  # <span style="color: purple">修正拼写错误</span>
        self.shouldMirrorPreview = shouldMirrorPreview
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        self._framesElapsed = 0  # <span style="color: purple">修正拼写错误</span>
        self._fpsEstimate = None  # <span style="color: purple">修正拼写错误</span>

    @property  # channel 定义了 channel 属性
    def channel(self):
        return self._channel

    @channel.setter  # 捕捉获取通道并清空当前帧缓存
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property  # frame 定义了 frame 属性
    def frame(self):
        if self._enteredFrame and self._frame is None:  # <span style="color: purple">修正拼写错误</span>
            _, self._frame = self._capture.retrieve(self._frame, self._channel)
        # 获取当前帧，如果捕获且未缓存，则从捕获对象中检索
        return self._frame

    @property  # 定义了指示是否正在写入图像文件属性
    def isWritingImage(self):  # <span style="color: purple">修正拼写错误</span>
        return self._imageFilename is not None

    @property  # 定义了指示是否正在写入视频文件属性
    def isWritingVideo(self):  # <span style="color: purple">修正拼写错误</span>
        return self._videoFilename is not None

    def enterFrame(self):  # <span style="color: purple">修正从 @property 改为方法</span>
        """Capture the next frame, if any."""
        assert not self._enteredFrame, 'previous enterFrame() had no matching exitFrame()'
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()  # <span style="color: purple">修正拼写错误</span>

    def exitFrame(self):  # 处理当前帧
        if self.frame is None:  # 检查是否存在帧
            self._enteredFrame = False
            return

        if self._framesElapsed == 0:  # 更新 fps
            self._startTime = time.time()
        else:
            timeElapsed = time.time() - self._startTime  # 从起始时间开始计算的时间
            self._fpsEstimate = self._framesElapsed / timeElapsed  # <span style="color: purple">修正拼写错误</span>
        self._framesElapsed += 1  # frameElapsed 用于记录已处理帧数

        if self.previewWindowManager is not None:  # 预览窗口处理，如果不为 None 则显示当前帧
            if self.shouldMirrorPreview:
                mirroredFrame = np.fliplr(self._frame)  # 若前置条件为真，则用 numpy.fliplr 水平镜像当前帧后显示
                self.previewWindowManager.show(mirroredFrame)  # <span style="color: purple">修正拼写错误</span>
            else:
                self.previewWindowManager.show(self._frame)  # 否则按原样显示帧

        if self.isWritingImage:
            cv2.imwrite(self._imageFilename, self._frame)  # 前置条件为真，则用 'cv2.imwrite' 写入到 “_imageFilename” 指定图像文件
            self._imageFilename = None

        self._writeVideoFrame()  # 调用 writeVideoFrame() 来处理视频帧写入

        self._frame = None
        self._enteredFrame = False  # 重置

    def writeImage(self, filename):
        self._imageFilename = filename

    def startWritingVideo(self, filename, encoding=cv2.VideoWriter_fourcc('M', 'P', '4', 'V')):
        """开始将处理完成的帧写入到一个视频文件中。"""
        self._videoFilename = filename
        self._videoEncoding = encoding

    def stopWritingVideo(self):
        """停止写入帧数到视频文件"""
        self._videoFilename = None
        self._videoEncoding = None
        if self._videoWriter:
            self._videoWriter.release()
            self._videoWriter = None

    def _writeVideoFrame(self):
        if not self.isWritingVideo:  # 初始化
            return
        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)  # 从视频捕获对象’self._capture‘中获得帧率
            if np.isnan(fps) or fps <= 0.0:  # fps 小于等于 0，无效
                if self._framesElapsed < 20:  # 已处理帧数小于 20，则返回不进行写入
                    return
                else:
                    fps = self._fpsEstimate  # 为 fps 估值
            size = (int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # <span style="color: purple">修正拼写错误</span>
            self._videoWriter = cv2.VideoWriter(self._videoFilename, self._videoEncoding, fps, size)
        self._videoWriter.write(self._frame)

class WindowManager(object):
    def __init__(self, windowName, keypressCallback=None):
        self.keypressCallback = keypressCallback
        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):  # <span style="color: purple">修正拼写错误</span>
        cv2.destroyWindow(self._windowName)  # <span style="color: purple">修正拼写错误</span>
        self._isWindowCreated = False  # <span style="color: purple">修正拼写错误</span>

    def processEvent(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            self.keypressCallback(keycode)
