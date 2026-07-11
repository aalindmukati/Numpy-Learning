import numpy as np

np.set_printoptions(suppress=True)

scalar = 5.0
print(scalar)
print('type of scalar',type(scalar))

print('-'*35)

# vector - 1D data
print('vector\n')


vector = np.array(
    [3,7,2]
)
print(vector)
print("shape of vector",vector.shape)

print('-'*35)


# Matrix - 2D data
print('Matrix\n')


Matrix = np.array(
    [[3,7,2],
    [2,3,9]]
)
print(Matrix)
print("shape of Matrix",Matrix.shape)

print('-'*35)

# Tensor - 3D data
print('Tensor\n')


Tensor = np.array(
    [
        [
            [1,2,3],
            [3,9,8]
        ],
        [
            [5,6,8],
            [11,23,4]
        ]
    ]
)
print(Tensor)
print("shape of Tensor",Tensor.shape)
print('-'*35)