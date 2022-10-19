import cv2
from util import *
import sys
buttonList=[]
def init():
  keys=[["C","D",'E',"F","G","A","B","C","D","E","F","G","A","B"],["C#","D#","F#","G#","A#","C#","D#","F#","G#","A#"]]
  class Button():
      def __init__(self,pos,text,size,color):
          self.pos=pos
          self.size=size
          self.text=text
          self.color=color
  for i in range(len(keys)):
      for j,key in enumerate(keys[i]):   
          if i==0:
              buttonList.append(Button([(j*70)+j*6+30,80],key,[70,200],(255,255,255)))
          else:
              buttonList.append(Button([(j*70)+j*31+65,80],key,[70,100],(0,0,0)))    


def playkeys(button):
    if button.text=="A":
        pyGamePlay("assets/A.wav")
    elif button.text=="B":
        pyGamePlay("assets/B.wav")      
    elif button.text=="C":
        pyGamePlay("assets/C.wav")
    elif button.text=="D": 
        pyGamePlay("assets/D.wav")
    elif button.text=="E":
        pyGamePlay("assets/E.wav")
    elif button.text=="F":  
        pyGamePlay("assets/F.wav")
    elif button.text=="G":
        pyGamePlay("assets/G.wav")

def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos
        w,h=button.size
        colorr=button.color
        cv2.rectangle(img,button.pos,(x+w,y+h),colorr,cv2.FILLED)
        cv2.putText(img,button.text,(x+10,y+h-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(214,0,220),2)
    return img    

def run(img,lmList,count,detector):
    img=drawAll(img,buttonList)
    if len(lmList) != 0:
        for button in buttonList:
            x,y=button.pos
            w,h=button.size
            for f in [4,8,12,16,20]:
                if x<lmList[f][1]<x+w and y<lmList[f][2]<y+h:
                    
                    l,_,_=detector.findDistance(lmList[f],lmList[f-3],img)
                    if l<135:
                      print("move you hand little closer",file=sys.stdout, flush=True)
                    elif l>150:
                      print("move you hand backward",file=sys.stdout, flush=True)
                    else:
                      print("stay there",file=sys.stdout, flush=True)
                    
                    
                    # print(l)
                    count+=1
                    if l<130 and (count==0 or count>50 and count<80):
                        try:
                            playkeys(button)
                            count=0
                        except Exception as e:
                            print(e)
                    if count>80:
                        count=0
    return count