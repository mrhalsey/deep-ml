import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    # Your code here
    vectors = np.asarray(vectors, dtype=float)
    norm = np.linalg.norm(vectors)

    basis = []
    for v in vectors:
        # Subtract the projection of v onto the existing basis vectors
        for b in basis:
            v -= np.dot(v, b) * b
        
        # Normalize the vector if it's not too small
        if np.linalg.norm(v) > tol:
            basis.append(v / np.linalg.norm(v))
    return basis