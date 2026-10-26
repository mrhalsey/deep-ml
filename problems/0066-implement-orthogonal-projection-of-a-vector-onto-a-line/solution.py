import numpy as np

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	#convert regular lists to np arrays
	v = np.asarray(v, dtype=float)
	L = np.asarray(L, dtype=float)

	proj = (np.dot(v, L) / np.linalg.norm(L)**2) * L
	return proj