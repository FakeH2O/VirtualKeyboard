from nis import cat
from unittest import expectedFailure
from warnings import catch_warnings
import numpy as np
import time
import cv2
# from cvzone.HandTrackingModule import HandDetector
import pygame

import HandTrackingModule as htm

cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector()
# window = pyglet.window.Window()
# detector =HandDetector(detectionCon=0.8)

keys=[["C","D",'E',"F","G","A","B","C","D","E","F","G","A","B"],["C#","D#","F#","G#","A#","C#","D#","F#","G#","A#"]]

class Button():
    def __init__(self,pos,text,size,color):
        self.pos=pos
        self.size=size
        self.text=text
        self.color=color
buttonList=[]
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):   
        if i==0:
            buttonList.append(Button([(j*70)+j*6+30,80],key,[70,200],(255,255,255)))
        else:
            buttonList.append(Button([(j*70)+j*31+65,80],key,[70,100],(0,0,0)))    

def playkeys(button):
    if button.text=="A":
        
        pygame.mixer.Sound("assets/A.wav").play()
        
        time.sleep(0.08)
        pygame.mixer.Sound("assets/A.wav").stop()
        
                
                
    elif button.text=="B":
            
        pygame.mixer.Sound("assets/B.wav").play()
        
        time.sleep(0.08)
        pygame.mixer.Sound("assets/B.wav").stop()
                
    elif button.text=="C":
            
        pygame.mixer.Sound("assets/C.wav").play()
        
        time.sleep(0.08)
        pygame.mixer.Sound("assets/C.wav").stop()
    elif button.text=="D":
            
        pygame.mixer.Sound("assets/D.wav").play()
        
        time.sleep(0.08)
        pygame.mixer.Sound("assets/D.wav").stop()
        
    elif button.text=="E":
            
        pygame.mixer.Sound("assets/E.wav").play()
        
        time.sleep(0.08)
        pygame.mixer.Sound("assets/E.wav").stop()
        

    elif button.text=="F":
            
        pygame.mixer.Sound("assets/F.wav").play()
        
        time.sleep(0.08)
        pygame.mixer.Sound("assets/F.wav").stop()
    elif button.text=="G":
            
        pygame.mixer.Sound("assets/G.wav").play()
        
        time.sleep(0.08)
        pygame.mixer.Sound("assets/G.wav").stop()


def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos
        w,h=button.size
        colorr=button.color
        cv2.rectangle(img,button.pos,(x+w,y+h),colorr,cv2.FILLED)
        cv2.putText(img,button.text,(x+10,y+h-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(214,0,220),2)
    return img    



    
    
        

count=0

while True:
    success,img=cap.read()
    pygame.init()
    img=cv2.flip(img,1)

    img = detector.findHands(img, draw=True )
    lmList = detector.findPosition(img, draw=False)
    img=drawAll(img,buttonList)
    if len(lmList) != 0:
        for button in buttonList:
            x,y=button.pos
            w,h=button.size
            for f in [4,8,12,16,20]:
                if x<lmList[f][1]<x+w and y<lmList[f][2]<y+h:
                    
                    l,_,_=detector.findDistance(lmList[f],lmList[f-3],img)
                    print(count)
                    count+=1
                    if l<120 and (count==0 or count>50 and count<80):
                        try:
                            playkeys(button)
                            count=0
                        except Exception as e:
                            print(e)
                    if count>80:
                        count=0
                    
                            

    key=cv2.waitKey(1)

    if key==ord('q'):
        break
                        
    cv2.imshow("IMAGE",img)
    
cap.release()
cv2.destroyAllWindows



