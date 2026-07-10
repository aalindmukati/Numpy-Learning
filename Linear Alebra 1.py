import numpy as np

np.set_printoptions(suppress=True)

scalar = 5.0
print(scalar)
print('type of scalar',type(scalar))

vector = np.array(
    [3,7,2]
)
print(vector)
print("shape of vector",vector.shape)

Matrix = np.array(
    [[3,7,2],
    [2,3,9]]
)
print(Matrix)
print("shape of Matrix",Matrix.shape)