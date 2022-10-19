import pygame
import time 

def pyGamePlay(file):
  pygame.init()
  pygame.mixer.Sound(file).play()
  time.sleep(0.08)
  pygame.mixer.Sound(file).stop()
