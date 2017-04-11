import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui as pg
np.set_printoptions(threshold=np.nan)

# Takes input from the game 
def screen_record(): 
    last_time = time.time()
    while(True): 
        frame =  np.array(ImageGrab.grab(bbox=(142,127,211,282)))
        # print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        frame = process_frames(frame)
        activation_value = 0              
        activation_value = Find_Activation_value(frame)
        print(activation_value)                             
        if(activation_value > 80):
            # print("jump")
            pg.keyDown('space')
            pg.keyUp('space')
            
        # cv2.imshow('window',frame)
        # print(pg.position())
        # pg.hotkey('space')
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# process image into simplyfied input
def process_frames(frame):
    Original_frame = frame
    # convert into gray
    processed_frame =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    # edge detection
    return processed_frame
     
# finds the activation_value
def Find_Activation_value(frame):
    value = 0
    for j in range (0,50):
        for i in range(j,154):
            # print(frame[i][0])
            if(frame[i][j] < 150):
                value = value + 1

            
    return value

screen_record();
