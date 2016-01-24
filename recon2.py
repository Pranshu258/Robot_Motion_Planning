from sklearn import manifold
import numpy as np
import os, sys
import Image
import matplotlib.pyplot as plt

if len(sys.argv) == 2:
	x = int(sys.argv[1])
	N = 0
	img_data = []
	rootDir = 'img/trajectory_1/'
	for dirName, subdirList, fileList in os.walk(rootDir):
	    for fname in fileList:
			img = Image.open(dirName + "/" + fname)
			img.load()
			data = (np.array(img)[0]).flatten()
			img_data.append(data)  
			N = N + 1
			if N > 10000:
				break 
	img_data = np.array(img_data)

	# Perform Isomap Manifold Learning
	clf = manifold.Isomap(n_neighbors=10, n_components=x)
	clf.fit(img_data)
	print x, clf.reconstruction_error()
	del img_data
	del clf