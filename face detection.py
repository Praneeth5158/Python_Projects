import cvzone
import cv2
cap=cv2.VideoCapture(0)
from cvzone.FaceDetectionModule import FaceDetector
detector = FaceDetector()
while True:
    sucess, img=cap.read()
    img=cv2.flip(img,1)
    img,bboxs =detector.findFaces(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)