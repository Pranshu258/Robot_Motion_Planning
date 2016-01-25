import numpy as np
from sklearn.neighbors import NearestNeighbors

train_data = np.genfromtxt('manifolds/manifold_2_1.csv', delimiter = ',')
test_data = np.genfromtxt('test/test_rand_trans.csv', delimiter = ',')

train_coords = np.genfromtxt('capture_points/captured1.csv', delimiter = ',')
test_coords = np.genfromtxt('test/random_points.csv', delimiter = ',')

nbrs = NearestNeighbors(n_neighbors=10)
nbrs.fit(train_data)
indices = nbrs.kneighbors(test_data, n_neighbors=10 ,return_distance=False)

err = 0
for i in xrange(1000):
	estimate_set = [train_coords[j] for j in indices[i]]
	mean_cor = np.divide(np.sum(estimate_set,0),10)
	actual_cor = test_coords[i]
	err = err + np.linalg.norm(actual_cor - mean_cor)/10.0

print "Localization Error for Circular Trajectory", err/1000.0