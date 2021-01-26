# -*- coding: utf-8 -*-
"""201701198_IE406_Lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wm8NSpY06Qvy8XOkfgMTeIGlRgj2uWes

Mounting the Google Drive.
"""

from google.colab import drive
drive.mount('/content/drive/')

"""Importing Libraries"""

import matplotlib.pyplot as plt 
import numpy as np
from sympy import *
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import math as mt

"""**-------------------------------------------------------------------------------------------**

Reading MNIST Training Dataset (.csv) file.
"""

df = pd.read_csv('/content/drive/My Drive/IE406- ML- Labs/Lab 4/mnist_train.csv')

"""Reading MNIST Testing Dataset (.csv) file."""

test_set = pd.read_csv('/content/drive/My Drive/IE406- ML- Labs/Lab 4/mnist_test.csv')
test = test_set.values

"""**-------------------------------------------------------------------------------------------**

Model.
"""

y = df['label']
prob = np.zeros([10,1])
for i in range(len(y)):
  prob[y[i]] = prob[y[i]] + 1

prob = prob/len(y)
#print(prob)

x0 = df[df['label']==0].drop(columns='label').values
x1 = df[df['label']==1].drop(columns='label').values
x2 = df[df['label']==2].drop(columns='label').values
x3 = df[df['label']==3].drop(columns='label').values
x4 = df[df['label']==4].drop(columns='label').values
x5 = df[df['label']==5].drop(columns='label').values
x6 = df[df['label']==6].drop(columns='label').values
x7 = df[df['label']==7].drop(columns='label').values
x8 = df[df['label']==8].drop(columns='label').values
x9 = df[df['label']==9].drop(columns='label').values

m0 = x0.mean()
m1 = x1.mean()
m2 = x2.mean()
m3 = x3.mean()
m4 = x4.mean()
m5 = x5.mean()
m6 = x6.mean()
m7 = x7.mean()
m8 = x8.mean()
m9 = x9.mean()

means = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9]
means = np.asarray(means)

c0 = np.cov(x0)
c1 = np.cov(x1)
c2 = np.cov(x2)
c3 = np.cov(x3)
c4 = np.cov(x4)
c5 = np.cov(x5)
c6 = np.cov(x6)
c7 = np.cov(x7)
c8 = np.cov(x8)
c9 = np.cov(x9)

c = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

c0i = np.linalg.pinv(c0)
c1i = np.linalg.pinv(c1)
c2i = np.linalg.pinv(c2)
c3i = np.linalg.pinv(c3)
c4i = np.linalg.pinv(c4)
c5i = np.linalg.pinv(c5)
c6i = np.linalg.pinv(c6)
c7i = np.linalg.pinv(c7)
c8i = np.linalg.pinv(c8)
c9i = np.linalg.pinv(c9)

c_inv = [c0i,c1i,c2i,c3i,c4i,c5i,c6i,c7i,c8i,c9i]
c_inv = np.asarray(c_inv)

mean_c = (c0 + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 )/10
c_minv = np.linalg.pinv(mean_c)

"""**-------------------------------------------------------------------------------------------**

Linear Discriminant Analysis.
"""

accuracy = 0
for i in range(len(test)):
  x = test[i,1:]
  minimum = 100000000000
  prediction = -1;
  for j in range(10):
    p = (x - means[j]).reshape(1,784)
    temp = np.matmul(p,np.matmul(c_minv,p.T))
    if temp < minimum:
      minimum = temp
      prediction = j
  
  if prediction == test[i,0]:
    accuracy = accuracy + 1
  
print('Accuracy of LDA =',accuracy*100/len(test),'%')

"""**-------------------------------------------------------------------------------------------**

Quadratic Discriminant Analysis.
"""

accuracy = 0
 for i in range(len(test)): 
   x = test[i,1:]
   maximum = -100000000000000;
   prediction = -1;
   for j in range(10):
     p = (x - means[j]).reshape(1,784)
     temp = -(np.matmul(p,np.matmul(c_inv[j],p.T)))/2 + mt.log(prob[j])
     if temp > maximum:
       maximum = temp
       prediction = j
  
   if prediction == test[i,0]:
     accuracy = accuracy + 1
  
print('Accuracy of QDA =',accuracy*100/len(test),'%')

"""**------------------------------------ END OF CODE ------------------------------------**"""