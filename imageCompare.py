import sys

import numpy
import imageio

#images should be of equal resolution
#cutoff is the percent of different pixels for the images to be counted as different
def compareImages (file1, file2, cutoff):

	image1 = toGrayscale(imageio.imread (file1))
	image2 = toGrayscale(imageio.imread (file2))
	cutoff = int (cutoff)

	difference = image1 - image2 #element-wise difference
	norm = numpy.linalg.norm(difference.ravel(), 0) #zero norm

	if (norm/(image1.shape[0] * image1.shape[1]) * 100 >= cutoff):
		return False
	else:
		return True


#converts images to grayscale
def toGrayscale(arr):
	if len(arr.shape) == 3:
		return numpy.average(arr, -1)  # average over the last axis (color channels)
	else:
		return arr

