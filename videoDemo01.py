import numpy as np
import cv2 as cv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cap = cv.VideoCapture('video.avi')
    while cap.isOpened():
        ret, frame = cap.read()
        # 如果正确读取帧，ret为True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(25) == ord('q'):
            break
# 完成所有操作后，释放捕获器

cap.release()
cv.destroyAllWindows()
