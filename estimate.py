from scipy.spatial import cKDTree
from sklearn import manifold
import numpy as np
import os
from PIL import Image
from operator import add

learner = manifold.Isomap(n_neighbors=10, n_components=3)

N = 0
img_data = []
rootDir = 'img/trajectory_1/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Loading the Learning Dataset: ' + dirName)
    for fname in fileList:
		img = Image.open(dirName + "/" + fname)
		img.load()
		data = (np.array(img)[0]).flatten()
		img_data.append(data) 
		#img.close() 
		N = N + 1
		if N > 9999:
			break 
rootDir = 'test/img_random/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Loading the Testing Dataset: ' + dirName)
    for fname in fileList:
		img = Image.open(dirName + "/" + fname)
		img.load()
		data = (np.array(img)[0]).flatten()
		img_data.append(data)
		#img.close()
img_data = np.array(img_data)

# Perform Isomap Manifold Learning
print "Running Isomap on the learning dataset ..."
train_data = learner.fit_transform(img_data[:10000])																														
print "Running Isomap on the test dataset ..."
test_data = learner.transform(img_data[10000:])
print "Saving the transformed test data to test_rand_trans.csv"
np.savetxt('test/test_rand_trans.csv', test_data, delimiter=',')