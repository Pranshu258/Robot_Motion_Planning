# Plot the data from a csv file containing the three Dimensional Manifold
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

if len(sys.argv) == 2:	
	image_type = int(sys.argv[1])
	# loading data from csv file
	print "Reading manifold data from: " + 'manifold_2_' + str(image_type) + '.csv'
	data = np.genfromtxt('manifolds/manifold_2_' + str(image_type) + '.csv', delimiter = ',', names = ['x', 'y', 'z'])
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.scatter(data['x'], data['y'], data['z'])
	ax.legend()
	plt.show()

else:
	data = np.genfromtxt('manifolds/manifold_1.csv', delimiter = ',', names = ['x', 'y', 'z'])
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.scatter(data['x'][:1000], data['y'][:1000], data['z'][:1000],color="red")
	ax.scatter(data['x'][1000:][:1000], data['y'][1000:][:1000], data['z'][1000:][:1000],color="blue")
	ax.scatter(data['x'][2000:], data['y'][2000:], data['z'][2000:],color="green")
	ax.legend()
	plt.show()