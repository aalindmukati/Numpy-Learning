import numpy as np

np.set_printoptions(suppress=True)

v1=np.array((1,3))
v2=np.array((4,2))

# print('v1=',v1)
# print('v2=',v2)

# dot = np.dot(v1,v2)
# print(dot)

#Euclidean Distance]

# diff = v1- v2

# print(diff)

# distance = np.linalg.norm(diff)

# print(distance)

# Multiplication and Linear Model 

# X = np.array([
#     [1,30],
#     [2,50],
#     [3,70]])

# print(X.shape)


# w = np.array([
#     [0.5],
#     [3]])

# print(w.shape)

# Xw = X @ w 
# print(Xw)


# bias = 2.0
# y = Xw + bias

# print(y)

data = np.array([
    [85, 26.6, 31, 0],
    [183, 23.3, 32, 1],
    [89, 28.1, 21, 0],
    [137, 43.1, 33, 1]
])
print ("Full data matrix: \n", data) 
print ("Data shape:", data. shape)