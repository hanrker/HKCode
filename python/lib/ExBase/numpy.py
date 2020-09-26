import numpy 
arr = numpy.array([1,2,3,4,5])
print(arr)
print(numpy.__version__)

arr2  = numpy.array(61)
print(arr2)

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(d.shape)

print(a.ndim) 
print(b.ndim) 
print(c.ndim) 
print(d.ndim)
print(d)



arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
y = arr.copy()
arr[0] = 61

print(arr) 
print(x)
print(y)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4))



arrh = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arrh.reshape(4,-1)
print(newarr)

for i in newarr:
    for j in i:
        print(j)    

import numpy as np
arr = np.array([11, 12, 13])
# aa = np.ndenumerate(?arr)
# print(aa)
for idx, x in arr:
  print(idx, x)

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arra = np.stack((arr1, arr2), axis=1)
arrb = np.concatenate((arr1, arr2), axis=2)
print(arra)
print(arrb)

