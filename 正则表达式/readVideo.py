import cv2 as cv
import numpy as np

def detectFaces(img):

    face_cascade = cv.CascadeClassifier("D:\Qt\opencv\etc\haarcascades\haarcascade_frontalface_default.xml")
    if img.ndim == 3:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)#1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []
    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result


cap = cv.VideoCapture("./test.mp4")

while(1):
    # get a frame
    ret, frame = cap.read()

    # show a frame
    result = detectFaces(frame)
    print(result)
    if len(result) > 0:
      point1 = (result[0][0],result[0][1])
      point2 = (result[0][2],result[0][3])
      cv.rectangle(frame,point1,point2,(0,0,255),5)
    cv.imshow("capture", frame)
    if cv.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
