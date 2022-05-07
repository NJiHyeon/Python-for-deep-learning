#1.numpy복습
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.zeros((2,3))
arr3 = np.arange(10) #0부터 10개까지의 배열
arr4 = np.random.randint(1,45,6) #1부터 45사이에서 6개 뽑기
print(arr1)
print(arr2)
print(arr3)
print(arr4)

#2. if, for, while
#배열 안에서 특정 원소를 뽑고 싶을 때
sub1 = arr3[0]
print(sub)
sub2 = arr3[0:3]
print(sub2)
sub3 = arr3[:3]
print(sub3)
sub4 = arr3[3:7]
print(sub4)
sub5 = arr3[3:9]
print(sub5)
sub6 = arr3[3:-1] #마지막 개수 숫자 적기 번거로울 때
print(sub6)


#조건문
sub = arr3[arr3<6]
print(sub)


#홀수 개수 구하는 방법
#간단한 방법
arr3 = np.arange(10)
arr3[arr3%2 == 1] #홀수 구하기
print(len(arr3[arr3%2 == 1]))

#조건문과 반복문을 사용하는 방법
count = 0
for i in range(len(arr3)) : 
    if arr3[i] % 2 == 1 :
        count = count +1
print(count)

#While문
i = 0
count = 0
while i < len(arr3) :
    if arr3[i] % 2 == 1 :
        count += 1
    i += 1
print(count)