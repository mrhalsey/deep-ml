import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		mean = np.mean(matrix, axis=1)
	if mode == "column":
		mean = np.mean(matrix, axis=0)
	return mean