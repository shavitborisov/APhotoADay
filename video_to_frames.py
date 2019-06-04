#!/usr/bin/python

import sys
import os
import cv2

def download_url(url):
    os.system("youtube-dl --id --restrict-filenames -f best " + url)

def cut_to_frames(f_name):
    folder = f_name[:-4] + "_frames" 
    os.mkdir(folder)

    vidcap = cv2.VideoCapture(f_name)
    count = 0

    while True:
        success, image = vidcap.read()
        if not success:
            break

        cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image) # save frame as JPG file
        count += 1

url_bank = tuple(open(sys.argv[1], 'r'))

for url in url_bank:
    print "Downloading video..."
    download_url(url)

    print "Cutting video to frames..."
    f_name = url[-11:] + ".mp4"
    cut_to_frames(f_name)

    print "Completed cutting frams for " + f_name
