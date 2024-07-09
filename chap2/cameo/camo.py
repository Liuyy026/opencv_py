import cv2
import numpy as np
from manager import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onkeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):  # 运行主程序
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                pass
            self._captureManager.exitFrame()
            self._windowManager.processEvent()  # <span style="color: purple">修正拼写错误</span>

    def onkeypress(self, keycode):
        if keycode == 32:  # 空格键
            self._captureManager.writeImage('/Users/liu/code/opencv_py/cameo/screenshot.png')
        elif keycode == 9:  # Tab 键
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('/Users/liu/code/opencv_py/cameo/screencast.mp4')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:  # Esc 键
            self._windowManager.destroyWindow()  # <span style="color: purple">修正拼写错误</span>

if __name__ == "__main__":
    Cameo().run()
