def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0]) != len(b[0]):
		return -1

	result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
	
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				result[i][j] += a[i][k] * b[k][j]
	return result