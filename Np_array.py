import numpy as np

arr1 = np.array([1,2,3,4,5]) #1D array
arr2 = np.array([[1,2,3],[4,5,6]]) #2d array
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]]) #3d array



# print(f'{arr1}\n')
# print("-------")
# print(f'{arr2}\n')
# print("-------")

# print(f'{arr3}\n')

print('shape=',arr2.shape)
print('dimension=',arr2.ndim)
print('data type=',arr3.dtype)
print('total element=',arr1.size)