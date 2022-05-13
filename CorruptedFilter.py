from os import listdir
import os
import cv2
import shutil
from collections import Counter

source_input = input("Please drag & drop the directory containing CORRUPTED images: ")
output = "E:\XXXXXXX\XXXXXXX\XXXXXXX" + '\\'
counter = 0

def nooutput():
     if os.path.exists(output):
        process()
     else:
        os.mkdir(output)
        process()
        
def process():
    for filename in listdir(source_input):
        if filename.endswith(("jpg", "jpeg", "bmp", "png")):
            try: 
                img = (filename)
                read = cv2.imread(img)
                cv2.imshow("IMAGE", read)
                cv2.waitKey(1)
                cv2.destroyAllWindows()
            except cv2.error as e:
                if e.err == "!_src.empty()":
                    global counter
                    counter+=1
                    print('ERROR ON FILE: ' + img + '  taking it out')
                    shutil.move(img, output)

nooutput()

print('CORRUPTED IMAGES = ', counter)
input("Press a key to close...")
