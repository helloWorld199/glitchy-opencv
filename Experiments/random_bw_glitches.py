import numpy as np
import cv2 as cv
import random
import math
from utils

random.seed(420)

HEIGHT = 540
WIDTH = 540
CHANS = 3
LINE_WIDTH = 2

blackImage = np.zeros((HEIGHT, WIDTH, CHANS), dtype=np.uint8) # To clear image
M = np.zeros((HEIGHT, WIDTH, CHANS), dtype=np.uint8) # Canvas
nCalls = 0

def random_bw_glitched_lines(event, x,y, flags, param):
    global blackImage, M, nCalls

    
    if event == cv.EVENT_MOUSEMOVE:
        if nCalls % 200 == 0:
            print("HERE!!!!!")
            M = np.zeros((HEIGHT, WIDTH, CHANS), dtype=np.uint8) # Reset canvas
            cv.imshow('out', blackImage)
        pos = random.random() * HEIGHT

        randR = math.ceil(random.random() * 255)
        randG = math.ceil(random.random() * 255)
        randB = math.ceil(random.random() * 255)
        print(randR, randG, randB)

        if pos > HEIGHT - LINE_WIDTH:
            pos = HEIGHT - LINE_WIDTH

        #print(int(pos))

        M[int(pos),:,0] = 100 
        M[int(pos),:,1] = 100
        M[int(pos),:,2] = 100

        cv.imshow('out', M)
        nCalls = nCalls + 1
        #print(nCalls)


blackImage = np.zeros((HEIGHT, WIDTH, CHANS))

cv.imshow('out', blackImage)

cv.setMouseCallback('out',random_bw_glitched_lines)

cv.waitKey(0)
cv.destroyAllWindows()