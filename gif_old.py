import imageio as io
import sys
import os

def gifFromFrames (directory, frameNumbers, duration):
	gif = []
	for number in frameNumbers:
		for filename in os.listdir(directory):
			if filename.endswith("{}.jpg".format(number)) or filename.endswith("{}.png".format(number)):
				gif.append(io.imread(directory + "/" + filename))
	io.mimsave(directory + '.gif', gif, duration = duration)


frames = []
for i in range(int(sys.argv[2])):
	frames.append(i*10)

gifFromFrames (sys.argv[1], frames, sys.argv[3])