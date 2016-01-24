from sklearn import manifold
import numpy as np
import os, sys
import Image
import matplotlib.pyplot as plt

xs = [1,2,3,4,5,6,7,8,9,10]

print "RECONSTRUCTION ERROR: PART 1"
N = 0
img_data = []
rootDir = 'img/part1/'
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
img_data = np.array(img_data)

# Perform Isomap Manifold Learning
errs1 = []
for x in xs:
	print "Learning Manifold with n_components: " + str(x)
	clf = manifold.Isomap(n_neighbors=10, n_components=x)
	clf.fit(img_data)
	errs1.append(clf.reconstruction_error())

del img_data
del clf

plt.plot(xs,errs1)
plt.show()