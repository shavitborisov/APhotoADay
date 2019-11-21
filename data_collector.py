#!/usr/bin/python

import sys
import os
import cv2

def download_url(url):
    os.system("youtube-dl --id --restrict-filenames -f best " + url)

url_bank = tuple(open(sys.argv[1], 'r'))

for url in url_bank:
    print "Downloading video..."
    download_url(url)

    print "Cutting video to frames..."
    f_name = url[-11:] + ".mp4"
    print f_name

    # cut_to_frames(f_name)

    print "Completed cutting frames for " + f_name