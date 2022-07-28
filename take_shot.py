import cv2
import keyboard
import os
from last_file import run

try:
    camera=cv2.VideoCapture(1)
    i=int(run())+1

    if os.path.isdir('./saved')==False:
        os.mkdir("./saved")

    os.chdir("./saved")

    while(keyboard.read_key()!='e'):
        input()
        ret, frame = camera.read()
        cv2.imwrite(str(i)+'.jpg', frame)
        i=i+1

    print("Exit is succesful")
    del(camera)

except:
    print("NO CAMERA DETECTED")
    exit()

