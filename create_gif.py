#!/usr/bin/python3.6

# Generates gif to current folder, from png frames in path_to_frames folder.
# Input: delay (recommended 10), path_to_frames, output (gif name will be output.gif).

import sys
import os

def gif_create(delay, path_to_frames, output):
    os.system("convert -delay " + delay + " -loop 0 " + path_to_frames + "*.png " + output + ".gif")

gif_create(sys.argv[1], sys.argv[2], sys.argv[3])
print (sys.argv[3] + ".gif generated successfully")
