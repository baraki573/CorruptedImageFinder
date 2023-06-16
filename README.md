# CorruptedImageFinder
It searches for corrupted images in the given path and moves the hits to a folder.
Afterwards, if you have (hopefully valid) backups, you can automatically collect
the affected files.
The script can also handle backups sorted in directories like:

```
year
└── month
	└── YYYYMMDD(*).jpg

```

Note, that in this case the image files' names have to follow the above format.

## Requeriments:
Python 3 (tested with 3.10.11);
shutil;
skimage

