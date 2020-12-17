#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Used in ML, DL and Reinforcement Learning


# In[22]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[23]:


a=np.array([0,1,2])
b=np.array([4,5,6,7])

a,b=np.meshgrid(a,b)

print(a)
print(b)


# In[29]:


fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot_surface(a,b,a**2+b**2,cmap="rainbow") #x,y,z, cmap="rainbow" or "coolwarm"
plt.show()


# In[30]:


a=np.arange(-1,1,0.02)
b=a

a,b=np.meshgrid(a,b)


# In[31]:


fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot_surface(a,b,a**2+b**2,cmap="rainbow") #x,y,z, cmap="rainbow" or "coolwarm"
plt.show()


# # Contour Plot

# In[32]:


fig = plt.figure()
ax = fig.gca(projection="3d")
ax.contour(a,b,a**2+b**2,cmap="rainbow") #x,y,z, cmap="rainbow" or "coolwarm"
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




