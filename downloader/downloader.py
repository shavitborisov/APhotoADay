# youtube-dl.exe should be in the same directory

import sys
import os

def downloadURL(url):
	os.system (".\youtube-dl.exe --id -f 22 --write-description --write-info-json " + url)

url = sys.argv[1]
start_age = sys.argv[2]
end_age = sys.argv[3]

downloadURL(url)