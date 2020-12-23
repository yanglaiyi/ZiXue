import numpy as np
import pandas as pd

s = np.array([['a','b','c','d','message'],[1, 2, 3, 4, "hello"],[5, 6, 7, 8, "world"],[9, 10, 11, 12, "foo"]])
s1 = np.array([[1, 2, 3, 4, "hello"],[5, 6, 7, 8, "world"],[9, 10, 11, 12, "foo"]])
print(s)

dataframe = pd.DataFrame(s)
dataframe1 = pd.DataFrame(s1)

dataframe.to_csv("Y:\ZhuoMian\ex1.csv",index=False,sep=',')
dataframe1.to_csv("Y:\ZhuoMian\ex2.csv",index=False,sep=',')

# df = pd.read_csv('Y:\ZhuoMian\ex1.csv')
# df = pd.read_csv('Y:\ZhuoMian\ex2.csv',header=None)

pd.read_csv('Y:\ZhuoMian\ex2.csv', names=['a', 'b', 'c', 'd', 'message'])