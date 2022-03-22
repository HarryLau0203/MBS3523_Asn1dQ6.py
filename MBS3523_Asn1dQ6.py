import cv2
import numpy as np
print(cv2.__version__)

cam = cv2.VideoCapture(0)
EVT = 0

def draw_rectangle(event,x,y,flags,param):
    global EVT
    global PNT1, PNT2
    if event == cv2.EVENT_LBUTTONDOWN:
        PNT1 = (x, y)
        EVT = event
    if event == cv2.EVENT_LBUTTONUP:
        PNT2 = (x, y)
        EVT = event
    if event == cv2.EVENT_RBUTTONDOWN:
        EVT = event

cv2.namedWindow('MBS3523')
cv2.setMouseCallback('MBS3523', draw_rectangle)
while True:
    success, img = cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1d-Q6 Name:Lau Chi Wing', (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                (0, 0, 255), 2)
    if EVT == 4:
        cv2.rectangle(img, PNT1, PNT2,(255,0,0),2)
        roi = img[PNT1[1]:PNT2[1],PNT1[0]:PNT2[0]]
        cv2.imshow('image ROI',roi)
    cv2.imshow('MBS3523',img)
    if EVT == 5:
        cv2.destroyAllWindows('image ROI')
        EVT = 0
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
