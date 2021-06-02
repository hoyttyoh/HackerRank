# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import pandas as pd
import numpy as np

# empty lists for data
Xtrain = []
Ytrain = []
Xtest = []

# convert input to something useful
for i,line in enumerate(sys.stdin):
    x = line.replace("\n","").split(" ")
    xs = np.asarray([np.float(j) for j in x])
    
    if i==0:
      
        i_train_start = 1
        i_train_end = xs[1]
        i_test_start = i_train_end + 1

    if (i > 0) and (i < i_train_end):
       
        Xtrain.append(xs[:-1])
        Ytrain.append(xs[-1])
        
    if i > i_test_start:
    
        Xtest.append(xs)

# convert all to array type
Xtrain = np.asarray(Xtrain)
Ytrain = np.asarray(Ytrain)
Xtest = np.asarray(Xtest)

from sklearn import linear_model

# simple linear model
lm = linear_model.LinearRegression()
lm.fit(Xtrain,Ytrain)

# predict house prices based on new input
ypred = lm.predict(Xtest)

# print out each prediction
for x in ypred:
    print(x)
