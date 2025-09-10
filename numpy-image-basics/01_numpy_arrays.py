import numpy as np

mylist = [1,2,3]

type(mylist)

myarray = np.array(mylist)

type(myarray)

np.arange(0,10, 2)

# lines x colums
np.zeros(shape=(5,5))

type(0)

np.ones(shape=(2,4))

np.random.seed(101)
arr = np.random.randint(0,100,10)

arr2 = np.random.randint(0,100,10)

arr.max()

arr.min()

arr.argmax()

arr.argmin()

arr.mean()

arr.shape

arr.reshape((2,5))

mat = np.arange(0,100).reshape(10,10)

mat.shape

row=0
col=1

mat[row,col]

mat[:,1].shape
mat[:,1].reshape(1,10)

mat[0:3,0:3]

