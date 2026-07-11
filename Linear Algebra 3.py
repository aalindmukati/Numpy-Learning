import numpy as np

# Two vectors with same length
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("v1:", v1)
print("v2:", v2)

# vector addition
v_add = v1 + v2
print("\nVector addition:", v_add)

# scalar multiplication
v1_scaled = 2 * v1
print("Scalar multiplication 2 * v1:", v1_scaled)

# Matrix example
A = np.array(
    [
    [3,4],
    [1,9]
    ]
)

B = np.array(
    [
        [2,6],
        [12,8]
    ]
)

matrix_add = A + B
print('matrix additon\n',matrix_add)

#transpose

A_transpose = A.T
print('Transpose\n',A_transpose)