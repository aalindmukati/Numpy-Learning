import numpy as np
import random

arr1 = np.array([1,2,3,4,5]) #1D array
arr2 = np.array([[1,2,3],[4,5,6]]) #2d array
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]]) #3d array



# print(f'{arr1}\n')
# print("-------")
# print(f'{arr2}\n')
# print("-------")

# print(f'{arr3}\n')

# print('shape=',arr2.shape)
# print('dimension=',arr2.ndim)
# print('data type=',arr3.dtype)
# print('total element=',arr1.size)

zeros = np.zeros([2,3])
print(zeros)
random_arr = np.random.rand(2,2)
print(random_arr)
eye = np.eye(3,3)
print(eye)

#doen