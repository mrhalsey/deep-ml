
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
    dot_product = np.dot(v1, v2)

    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    cos = dot_product / ((norm_v1 * norm_v2))
	return round(cos, 3)
