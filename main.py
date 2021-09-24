# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import dlib, cv2



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("hello word")
    f = "D:/1231.jpg"
    detector = dlib.get_frontal_face_detector()
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    dets = detector(img, 1)
    for index, face in enumerate(dets):
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()  # 绘制人脸的边框，边框宽度为3   cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),3)
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
    cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()