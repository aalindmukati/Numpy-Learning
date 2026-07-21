import numpy as np

np.set_printoptions(suppress=True)

v1=np.array((1,3))
v2=np.array((4,2))

# print('v1=',v1)
# print('v2=',v2)

# dot = np.dot(v1,v2)
# print(dot)

#Euclidean Distance]

diff = v1- v2

print(diff)

distance = np.linalg.norm(diff)

print(distance)