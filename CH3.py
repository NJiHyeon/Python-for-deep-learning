#1. function
from tkinter import N
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([0,4,4])
print(arr1)
print(arr2)

#2. 복습
odd1 = len(arr1[arr1%2==1])
print(odd1)
odd2 = len(arr2[arr2%2==1])
print(odd2)
#array를 만들때마다 복사를 해주어야 하기 때문에 번거롭다 -> 공통된 식을 함수로 한번에 묶기

#개수의 함수
def odd(arr) : 
    n = len(arr[arr%2==1])
    print(n)

odd(arr1)
odd(arr2)

#값의 함수
def odd(arr) : 
    n = len(arr[arr%2==1])
    return n
