from os import listdir
import os
#import cv2
from PIL import Image
import shutil
from collections import Counter
import glob

source_input = input("Please drag & drop the directory containing CORRUPTED images: ")
source_dir = (source_input)
source_dir = source_dir.strip('"')
source_dir2 = source_dir.replace('[', 'o[o')
source_dir2 = source_dir2.replace(']', 'o]o')
source_dir2 = source_dir2.replace('o[o', '[[]')
source_dir2 = source_dir2.replace('o]o', '[]]')
source_dirclean = source_dir2.replace('#', '[#]')
output = "E:\XXXXX\XXXXXXXX\XXXXXXXX" + '\\'
counter = 0

def nooutput():
     if os.path.exists(output):
        process()
     else:
        os.mkdir(output)
        process()
        
def process():
    for filename in glob.iglob(source_dirclean + '/**/*.*', recursive=True):
        if filename.endswith(("jpg", "JPG", "jpeg", "JPEG", "bmp", "BMP", "png", "PNG")):
            #breakpoint()
            try:
                img = (filename)
                imge = Image.open(filename)
                imge.verify()
                #read = cv2.imread(img)
                #cv2.imshow("IMAGE", read)
                #cv2.waitKey(50)
                #cv2.destroyAllWindows()
            except (IOError, SyntaxError) as e:
            #except cv2.error as e:
                #if e.err == "!_src.empty()":
                    global counter
                    counter+=1
                    print('ERROR ON FILE: ' + img + '  taking it out')
                    shutil.move(img, output)

nooutput()

print('CORRUPTED IMAGES = ', counter)
input("Press a key to close...")
