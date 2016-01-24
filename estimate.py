from scipy.spatial import cKDTree
from sklearn import manifold
import numpy as np
import os
import Image

learner = manifold.Isomap(n_neighbors=10, n_components=3)

print "ANALYSIS OF THE RANDOM POINTS DATASET"
print "================================================"

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
		N = N + 1
		if N > 10000:
			break 
rootDir = 'test/img_random/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Loading the Testing Dataset: ' + dirName)
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
print "Running Isomap on the dataset ..."
data = learner.fit_transform(img_data)
del img_data
learned_data = data[:10000]
test_data = data[10000:]
del data

# Find the nearest neighbor in learned data for each entry in test data
print "Analyzing the results ..."
dataTree = cKDTree(learned_data)
indexes = dataTree.query(test_data)[1]

coord_data = np.genfromtxt('capture_points/captured1.csv', delimiter = ',', names = ['x', 'y', 't'])
coord_data = np.array([coord_data['x'], coord_data['y'], coord_data['t']]).T

actual_data = np.genfromtxt('test/random_points.csv', delimiter = ',', names = ['x', 'y', 't'])
actual_data = np.array([actual_data['x'], actual_data['y'], actual_data['t']]).T

print "Calculating the Localization Error ..."
i = 0
err = 0
for index in indexes:
	estimated_coord = coord_data[index]
	actual_coord = actual_data[i]
	err = err + np.linalg.norm(actual_coord - estimated_coord)/1000
	i = i + 1
print "Localization Error: " + str(err)
print "------------------------------------------------"

#############################################################################################################

print "ANALYSIS OF THE RADIAL TRAJECTORY DATASET"
print "================================================"

N = 0
img_data = []
rootDir = 'img/trajectory_3/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Loading the Learning Dataset: ' + dirName)
    for fname in fileList:
		img = Image.open(dirName + "/" + fname)
		img.load()
		data = (np.array(img)[0]).flatten()
		img_data.append(data)  
		N = N + 1
		if N > 10000:
			break 
rootDir = 'test/img_radial/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Loading the Testing Dataset: ' + dirName)
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
print "Running Isomap on the dataset ..."
data = learner.fit_transform(img_data)
del img_data
learned_data = data[:10000]
test_data = data[10000:]
del data

# Find the nearest neighbor in learned data for each entry in test data
print "Analyzing the results ..."
dataTree = cKDTree(learned_data)
indexes = dataTree.query(test_data)[1]

coord_data = np.genfromtxt('capture_points/captured3.csv', delimiter = ',', names = ['x', 'y', 't'])
coord_data = np.array([coord_data['x'], coord_data['y'], coord_data['t']]).T

actual_data = np.genfromtxt('test/radial_points.csv', delimiter = ',', names = ['x', 'y', 't'])
actual_data = np.array([actual_data['x'], actual_data['y'], actual_data['t']]).T

print "Calculating the Localization Error ..."
i = 0
err = 0
for index in indexes:
	estimated_coord = coord_data[index]
	actual_coord = actual_data[i]
	err = err + np.linalg.norm(actual_coord - estimated_coord)/1000
	i = i + 1
print "Localization Error: " + str(err)
print "------------------------------------------------"