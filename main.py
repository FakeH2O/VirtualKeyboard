from nis import cat
from unittest import expectedFailure
from warnings import catch_warnings
import numpy as np
import time
import cv2
# from cvzone.HandTrackingModule import HandDetector
import pyglet
import HandTrackingModule as htm

cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector()
window = pyglet.window.Window()
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
            buttonList.append(Button([(j*70)+j*5+20,80],key,[70,200],(255,255,255)))
        else:
            buttonList.append(Button([(j*70)+35+j*30+20,80],key,[70,100],(0,0,0)))    

def playkeys(button):
    if button.text=="A":
            
        effectA=pyglet.resource.media("assets/A.wav",streaming=False)
        effectA.play()
                
                
    elif button.text=="B":
            
        effectB=pyglet.resource.media("assets/B.wav",streaming=False)
        effectB.play()
                
    elif button.text=="C":
            
        effectC=pyglet.resource.media("assets/C.wav",streaming=False)
        effectC.play()
    elif button.text=="D":
            
        effectD=pyglet.resource.media("assets/D.wav",streaming=False)
        effectD.play()
    elif button.text=="E":
            
        effectE=pyglet.resource.media("assets/E.wav",streaming=False)
        effectE.play()
        

    elif button.text=="F":
            
        effectF=pyglet.resource.media("assets/F.wav",streaming=False)
        effectF.play()
    elif button.text=="G":
            
        effectG=pyglet.resource.media("G.wav",streaming=False)
        effectG.play()                  


def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos
        w,h=button.size
        colorr=button.color
        cv2.rectangle(img,button.pos,(x+w,y+h),colorr,cv2.FILLED)
        cv2.putText(img,button.text,(x+10,y+h-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(214,0,220),2)
    return img    



    
    
        



while True:
    success,img=cap.read()
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
                    print(l)
                    if l<120:
                        try:
                            playkeys(button)
                        except:
                            print("error")
                            
                            

    key=cv2.waitKey(1)

    if key==ord('q'):
        break
                        
    cv2.imshow("IMAGE",img)
    
cap.release()
cv2.destroyAllWindows



