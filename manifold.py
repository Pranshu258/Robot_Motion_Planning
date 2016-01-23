# Learn the manifold for images present in a given directory

import Image
import numpy as np
from sklearn import manifold
import os, sys

if len(sys.argv) == 2:	
	image_type = int(sys.argv[1])

# Creating the Dataset for the Images
img_data = []

N = 1 		# Number of images to process for learning the manifold
if len(sys.argv) == 2:
	rootDir = 'img/trajectory_' + str(image_type)
else:
	rootDir = 'img/part1/'

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Traversing : ' + dirName)
    for fname in fileList:
		img = Image.open(dirName + "/" + fname)
		img.load()
		data = (np.array(img)[0]).flatten()
		img_data.append(data)
		print N   
		N = N + 1
		if N > 10000:
			break 

# The Image Dataset, as anumpy array of arrays of pixels
print "Creating the numpy array"
img_data = np.array(img_data)
# Variables for manifold learning.
n_neighbors = 10
# Perform Isomap Manifold Learning
print "Learning the Manifold"
trans_data = manifold.Isomap(n_neighbors, n_components=3).fit_transform(img_data)

if len(sys.argv) == 2:
	print "Saving the transformed data to manifold_2_" + str(image_type) + ".csv"
	np.savetxt('manifolds/manifold_2_' + str(image_type) + '.csv', trans_data, delimiter=',')
else:
	print "Saving the transformed data to manifold_1.csv"
	np.savetxt('manifolds/manifold_1.csv', trans_data, delimiter=',')
