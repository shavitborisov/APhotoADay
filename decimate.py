# make a new folder with every ith frame

import os
import sys

folder = sys.argv[1]
factor = sys.argv[2]

for i in range(len(os.listdir(folder))):
	for filename in os.listdir(folder):
	    if filename.endswith("{}.jpg".format(i)) or filename.endswith("{}.png".format(i)):
	    	if i%int(factor) != 0:
	    		os.remove (folder + "/" + filename)
	    
