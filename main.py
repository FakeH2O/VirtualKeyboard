import numpy as np
import cv2
import HandTrackingModule as htm
import keyboard
import drum



hands=2
choice=input("What do you like to play: 1->keyboard 2->drum:")
if choice=="1":
    keyboard.init()
    hands=1
else:
    hands=2

cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)  
detector = htm.handDetector(maxHands=hands,detectionCon=0.8)



count=0

while True and choice=="1" or choice == "2":
    success,img=cap.read()
    img=cv2.flip(img,1)
    img = detector.findHands(img, draw=True )

    lmList = detector.findPosition(img,draw=False)
    if choice=="1":
        count=keyboard.run(img,lmList,count,detector)
    else:
        count=drum.run(img,lmList,count)    
    key=cv2.waitKey(1)
    

    if key==ord('q'):
        break
                        
    cv2.imshow("IMAGE",img)
    
cap.release()
cv2.destroyAllWindows



