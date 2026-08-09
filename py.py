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

z=input("enter the number")
print(z)
