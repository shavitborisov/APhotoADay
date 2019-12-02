import sys
import os
import numpy
import PIL
import imageio

img_names = os.listdir(sys.argv[1])
initial_age = int(sys.argv[2]) * 365

files = sorted(img_names,key=lambda x: int(os.path.splitext(x)[0]))
toCheck = enumerate(files)

for i, img in toCheck:
	os.rename(img, "age{}.jpg".format(initial_age + i))

for img in os.listdir(sys.argv[1]):
	os.rename(img, img[3:])