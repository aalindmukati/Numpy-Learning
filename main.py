import numpy as np
import time
# print(np.__version__)

n = 1_000_000 #this is the same way of saying 1million but the underscore acts like the comma 1,000,000

py_list = list(range(n))
np_array = np.arange(n)

# print(py_list[0:5])
# print(np_array[0:5])

t1 = time.time()
py_result=[x*2 for x in py_list]
t2 = time.time()

ttt = t2-t1

t3 = time.time()
py_result=np_array * 2
t4 = time.time()

tt = t4-t3
a =[]

for x in py_list:
    a.append(x*2)

# print(len(a))
# print(a[:5])
# print(py_list[:5])

# print(f"numpy time {tt:.9f}")

# print(f"list time {ttt:.9f}")

arry = np.array([[1,4,6],
                 [7,2,5],
                 [9,8,3]])

print(arry[1,1]) #Indiv element
print(arry[0]) #row access
print(arry[:,2]) #coloumn access