
# coding: utf-8

# In[3]:



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.optimize import fmin_cg


# In[4]:

#import data


def load(filename):
    '''
    filenname: string ('test.csv')

    returns: DataFrame
    '''
    data = pd.DataFrame.from_csv(filename, encoding = 'utf-8')
    print '\nData Columns:'
    for i in range(len(data.columns)):
        print '\t',i,'\t', data.columns[i]

    check(data)

    return data

def check(X):
    '''
    X: DataFrame or Series

        prints shape and head

    returns: None
    '''
    print '\nShape is:\n', X.shape
    print X.head()

data = load('cs-training.csv')


# In[5]:

'''
# Shuffle index
index = np.array(data.index)
random.shuffle(index)

print index.shape
print index

# training set (60%)
trainingSize = data.shape[0] * 0.60
training = data.ix[index[:trainingSize]]

training.to_csv('training.csv', encoding='utf-8')

print '\n', training.shape
print training.head()

# crossValidation set (20%)
crossValSize = data.shape[0] * 0.20
crossValidation = data.ix[index[trainingSize:trainingSize + crossValSize]]

crossValidation.to_csv('crossValidation.csv', encoding='utf-8')

print '\n', crossValidation.shape

# test set (20%)
test = data.ix[index[trainingSize + crossValSize:]]

test.to_csv('test.csv', encoding = 'utf-8')

print '\n', crossValidation.shape
'''


# In[6]:

# load files

training = load('training.csv')
crossValidation = load('crossValidation.csv')
test = load('test.csv')


# In[7]:

# 0. PROCESS DATA (-> X, y)
    # X
    # y
    # feature scaling

# I. TRAIN (-> theta)
    # theta = fmincg(CostFunction, X, y, lambda, initial_theta)

# (J, grad) = CostFunction(X, y, lambda)

# II. PREDICT (-> h(x))

# h = predict(X)

# III. GET ACCURACY & F-SCORE


# # 0. PROCESS DATA (-> Xtrain, ytrain)
# ##Xtrain
# ##ytrain
# ##featureScale
# ##addBias

# In[ ]:

# 0. PROCESS DATA (-> X, y)
Xtrain = training.iloc[:, 1:]
check(Xtrain)
(m, n) = Xtrain.shape # m: # of examples /n: # of attributes

ytrain = training['SeriousDlqin2yrs']
check(ytrain)

# feature scaling
def featureScale(X):
    '''
    X: DataFrame

    returns: DataFrame (feature scaled)
    '''
    for col in range(X.shape[1]):
        #print 'col index:', col
        copied = X.iloc[:, col]
        #print 'head\n', copied.head()
        #print 'mean: ', copied.mean()
        #print 'std: ', copied.std()
        X.iloc[:, col] = (copied - copied.mean())/copied.std()
    return X

Xtrain = featureScale(Xtrain)
check(Xtrain)

# Add Bias terms to Xtrain
def addBias(X):
    '''
    X: DataFrame (m * n)

        Adds bias terms to the first column

    returns: DataFrame (m * (n + 1))
    '''
    X.insert(0, 'Bias', 1)
    return X

Xtrain = addBias(Xtrain)
check(Xtrain)


# # I. TRAIN (-> theta)
# ## theta = fmin_cg(CostFunction, X, y, lambda, initial_theta)
# ## J = costFunction(X, y, lambda)
# ## grad = gradFunction

# In[ ]:


'''
# logisticRegression

L = 0.1

def logisticRegression(costfunction, X, y, L):
    \'''
    constFunction: function
    X: matrix
    y: vector
    L (lambda): float

    returns: vector (theta)
    \'''
    theta = fmin_cg(f = costFunction, x0 = X, fprime = gradFunction)
    return theta

# costFunction
def costFunction(theta, (X, y, L)):
    \'''
    theta: vector
    X: matrix
    y: vector
    L (lambda): float

    returns: float (J)
    \'''
    J = sum(np.multiply(np.log(sigmoid(X.dot(theta))), -y) -            np.multiply((1 - y),log(1 - sigmoid(X.dot(theta)))))/m
    J = J + (L/(2*m)) * sum(theta[1:]**2)

    return J

# gradFunction
def gradFunction(grad):
    # grad = transpose(sigmoid(X * y)) * y + lambda * sum(theta[1:])/m
    return grad

# sigmoid
def sigmoid(z):
    \'''
    x: float

    returns: float
    \'''
    return 1.0/(1.0 + np.exp(-z))


#theta = logisticRegresssion()
theta = np.ones((n+1, 1))
J = costFunction(theta, (Xtrain, ytrain, L))
print 'J', J
'''
# In[ ]:




# In[ ]:




# In[ ]:

# Learning Curve


# In[ ]:

test.iloc[3, :]


# In[ ]:

test.ix[3]


# In[ ]:
