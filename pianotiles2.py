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
        # only 4 tiles image is captured at a time
        # which is then processesed
        frame =  np.array(ImageGrab.grab(bbox=(10,290,191,303)))
        last_time = time.time()
        frame = process_frames(frame)
        Find_key(frame);
        # cv2.imshow('window',frame)
        # print(pg.position())
        # pg.hotkey('space')
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# process image into simplyfied input (grayed image)
def process_frames(frame):
    Original_frame = frame
    # convert into gray
    processed_frame =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    return processed_frame


# finds which key to press (numbers here show pixels which is to be checked if there is black tile)
# game ran using nox player in top(0,0) cordinate
def Find_key(frame):
   
    if(frame[10][30] < 150):
        pg.hotkey('a');
    if(frame[10][75] < 150):
        pg.hotkey('s');
    if(frame[10][110] < 150):
        pg.hotkey('d');
    if(frame[10][155] < 150):
        pg.hotkey('f');



screen_record();
