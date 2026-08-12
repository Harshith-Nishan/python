# # h="haibro" g
# # print(h[-5:-1])

# list=[1,'gfg',6.6]
# lists=[1,'gfg',6.8]
# #print(list,lists)
# #list.append(lists)
# list.insert(3,66)
# print(list)
# list.pop()
# print(list)
# list.append(9)
# print(list)
# del list[1:]
# print(list)
# list.extend(lists)
# print(list)
# list.extend([1,2,3])
# print(list)
# list.sort
# print(list)

# tuple=(2,4,5,6,7,8,'rt',6)

# print(tuple.count(6))
# sett={7,5,6,8,9,4,3,2,1,67,88}
# print(sett)

# sett.add(10)
# dic={1:'h',2:'a'}
# print(dic)
# print(dic['h'])
# dic.get(2)

# dic={
#      1:'hai',
#      1:['hello','bro'],
#      2:{'a':'haibro'}
#      }

# print(dic[])

# a=10
# b=a
# print(id(a))
# print(id(b))
# a=11
# print(id(a))
# print(id(b))
# range(10)
# print(range(10))
# print(list(range(10)))
# n=-(7)
# print(n)

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import sklearn

# print("NumPy version:", np.__version__)
# print("Pandas version:", pd.__version__)
# print("Scikit-learn version:", sklearn.__version__)

# print("All libraries installed successfully!")
# import pandas as pd
# from sklearn.decomposition import PCA

# # Sample dataset
# data = {
#     "Height": [150, 160, 170, 180, 190],
#     "Weight": [50, 60, 70, 80, 90]
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# print("Original Data:")
# print(df)

# # Create PCA object (Reduce to 1 Principal Component)
# pca = PCA(n_components=1)

# # Fit and Transform
# pc = pca.fit_transform(df)

# print("\nPrincipal Component:")
# print(pc)

# print("\nEigenvalue:")
# print(pca.explained_variance_)

# print("\nEigenvector:")
# print(pca.components_)

# print("\nVariance Ratio:")
# print(pca.explained_variance_ratio_)

# from math import sqrt 

# print(sqrt(7))

# z=input("enter the number")
# print(z)
# list=[1,'gfg',6.6]
# lists=[1,'gfg',6.8]
# #print(list,lists)
# #list.append(lists)
# list.insert(3,66)
# print(list)
# list.pop()
# print(list)
# list.append(9)
# print(list)
# del list[1:]
# print(list)
# list.extend(lists)
# print(list)
# list.extend([1,2,3])
# print(list)
# list.sort
# print(list)
# h=30
# if h>=30:
#     print("h is greater than 30")
# else if h<30:
#     print("h is less than 30")

# def check_even_odd(num):
#     print("The number is even" if num % 2 == 0 else "The number is odd")   
# h=40
# def calculate_total(numbers):
#     total = 0

#     for number in numbers:
#         total += number

#     return total


# def check_number(number):
#     if number > 50:
#         return "Greater than 50"
#     elif number == 50:
#         return "Exactly 50"
#     else:
#         return "Less than 50"


# def main():
#     numbers = [10, 25, 50, 75, 100]

#     print("Starting program")

#     total = calculate_total(numbers)
#     average = total / len(numbers)

#     print("Total:", total)
#     print("Average:", average)
#     import math as pdd

#     for number in numbers:
#         result = check_number(number)
#         print(number, "→", result)

#     print("Program finished")


# main()
# for i in range(20, 1,-6):
#     pass
# dit={1: 'hello', 2: 'world'}

# for key in dit.keys():
#     print(key, dit[key])


# student = {
#     "name": "Harshith",
#     "age": 25,
#     "course": "ML"
# }

# for key in student.keys(),values(),items():
#     print(key, student[key])

# for i in range(4):
#     print("#")
#     for j in range(4):
#         print("#", end="")
#     print()
# x=10
# for x>1:
#     print(x)

# for i in range(1, 11):
#     i=1
#     if i > 5:
#         print(i)
# else:
#     print("Loop completed")from array
# from array import *
# arr=array('i',[2,3,4,5,6])
# for i in arr:
#     print(i)
#     print(arr.buffer_info())
# from numpy import *

# z=array("i",[])
# x=int(input("enter size"))

# for i in range(x):
#     y=int(input("enter the numbers"))
#     z.append(y)
# from array import array

# z = array("i", [])

# x = int(input("enter size"))

# for i in range(x):
#     y = int(input("enter the numbers"))
#     z.append(y)

# print(z)
# print
# print
# print.
# from numpy import *

# # arr=array([1,2,3,4,5,'g'])
# # print(arr)
# arr=logspace(1,10,2)
# print(arr)


# x=30
# a=x
# print(x,a)
# print(id(x))
# print(id(a))
# x=40
# print(id(x))
# print(id(a))
from numpy import *
arr=array([1,2,3,4,5])
arr2=arr.copy()
z=arr2*5
print(z)