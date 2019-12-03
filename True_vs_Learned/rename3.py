import sys
import os
import numpy
import PIL
import imageio

img_names = os.listdir(sys.argv[1])

files = sorted(img_names,key=lambda x: int(os.path.splitext(x)[0]))
toCheck = enumerate(files)

for i, img in toCheck:
	os.rename(img, "{}.png".format(0 + i))