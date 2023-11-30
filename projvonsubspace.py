# Define the inner product of two vectors
def inner_product(vec1, vec2):
    return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))

# Define the projection of vector x onto subspace with basis B
def projection_onto_subspace(x, B):
    coefficients = [inner_product(x, b) / inner_product(b, b) for b in B]
    projection = [sum(c * v for c, v in zip(coefficients, basis)) for basis in zip(*B)]
    return projection

# Starting vector
x = [-1, -1, 2, 2]

# Matrix of subspace basis vectors
B = [[0.707107, 0, 0.707107, 0],
     [0, 0.707107, 0, 0.707107]]

# Projecting the vector onto the subspace
proj_x = projection_onto_subspace(x, B)
print("Projected vector onto the subspace:", proj_x)
