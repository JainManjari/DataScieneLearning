#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d.axes3d


# In[2]:


X=pd.read_csv("Linear_X_Train.csv")
Y=pd.read_csv("Linear_Y_Train.csv")

X=X.values
Y=Y.values

#Normalisation

X=(X-X.mean())/X.std()


# In[7]:


theta_list=np.load("theta_list.npy")
T0=theta_list[:,0]
T1=theta_list[:,1]


# In[8]:


plt.ion() #"i" for interaction and "on" for on

for i in range(0,50,3):
    yp=T1[i]*X+T0[i]
    plt.scatter(X,Y)
    plt.plot(X,yp,'red')
    plt.draw()
    plt.pause(1)
    plt.clf()


# In[ ]:




