import sys
import os

def rename2(filename):
	for i, j in enumerate(filename):
		if j == '_':
			filename = filename[0 : i] + filename[i + 3 : len(filename)]
	return filename

for img in os.listdir(sys.argv[1]):
	os.rename(img, rename2(img))