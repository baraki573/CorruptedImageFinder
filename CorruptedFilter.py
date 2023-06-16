from os import listdir
import os
from skimage import io
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
output = "AAAA"
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
				imgf = io.imread(img)
			except:
				#if e.err == "!_src.empty()":
				global counter
				counter+=1
				print('ERROR ON FILE: ' + img + '  taking it out')
				try:
					shutil.move(img, output)
				except:
					print("File already exists")
				
def copy_backup():
	global output
	in_dir = output
	master = "BBBB"
	output = "CCCC"
	sort_year_month = True
	global counter
	counter = 0
	if not os.path.exists(output):
		os.mkdir(output)
	for corrupted in listdir(in_dir):
		if os.path.exists(f"{output}\\{corrupted}"):
			continue
		master_path = f"{master}\\{corrupted}"
		if sort_year_month:
			year = corrupted[0:4]
			month = corrupted[4:6]
			master_path = f"{master}\\{year}\\{month}\\{corrupted}"
		shutil.copy(master_path, f"{output}\\{corrupted}")
		counter+=1

nooutput()

print('CORRUPTED IMAGES = ', counter)
a = input("Press \"Y\" to copy the backups, other keys will exit: ")
if a.lower()=="y":
	copy_backup()
	print(f"{counter} files successfully copied!")