#1.연산
a = 1
b = 2
c = a + b
print(c)

a = 1.2
b = 2.4
print(a+b)

a = 's'
b = "q"
print(a+b)
print(a*b)

#2.여러가지 타입의 형태
a = True
b = False
print(a+b)
print(type(a))

aa = 4
print(type(a))

bb = 4.3
print(type(a))

cc = 'hi'
print(type(a))

list1 = [1,2,3,4]
arr = numpy.array([1,2,3,4])
tuple1 = (1,2)
print(type(list1))
print(type(arr))
print(type(tuple1))

#3.라이브러리
import numpy
#zeros, empty, ones, array, sum, .....
arr1 = numpy.array([1,2,3,4])
arr2 = numpy.zeros(4) #1행 4열짜리 영행렬

import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.zeros(4)
arr3 = np.ones(4)

from numpy import array, ones, zeros
arr1 = array([1,2,3,4])
arr2 = zeros(4)
arr3 = ones(4)

from random import sample
import numpy as np
import pandas as pd
import tensorflow as tf
