#!/usr/bin/env python
# coding: utf-8

# <center><img style="float: center; width:90%" src="https://raw.githubusercontent.com/Jeshua-Romero-Guadarrama/CienciaDatosPython/main/images/JeshuaNomics.png">
# </center><br>
# 
# <script src="https://kit.fontawesome.com/37a97f957d.js" crossorigin="anonymous"></script>
# 
# <center><a href="https://www.datascience.jeshuanomics.com/" target="blank" style="font-size:20px;">
# Introducción a la Ciencia de Datos para Economistas en Python
# </a></center>
# 
# <center><a href="https://www.jeshuanomics.com/" target="blank" style="font-size:20px;">
# Publicado por Jeshua Romero Guadarrama en colaboración con JeshuaNomics
# </a></center>
#     
# <center><a href="https://www.jeshuanomics.com/" target="blank">
# ____________________________________________________________________________________________________
# </a></center><br>
# 
# <center>
# <a href="https://github.com/JeshuaNomics"><i class="fa fa-github" aria-hidden="true"></i><span class="label"></span> GitHub  </a>
# <a href="https://www.facebook.com/JeshuaNomics/"><i class="fa fa-facebook" aria-hidden="true"></i><span class="label"></span> Facebook  </a>
# <a href="https://twitter.com/JeshuaNomics"><i class="fa fa-twitter" aria-hidden="true"></i><span class="label"></span> Twitter  </a>
# <a href="https://www.linkedin.com/in/jeshua-romero-guadarrama/"><i class="fa fa-linkedin" aria-hidden="true"></i><span class="label"></span> Linkedin  </a>
# <a href="https://vk.com/jeshuanomics"><i class="fa fa-vk" aria-hidden="true"></i><span class="label"></span> Vkontakte  </a>
# <a href="https://jeshuanomics.tumblr.com/"><i class="fa fa-tumblr" aria-hidden="true"></i><span class="label"></span> Tumblr  </a>
# <a href="https://www.youtube.com/channel/UCY7f84mJGvMN7TF7XI4-Jgg?view_as=subscriber/"><i class="fa fa-youtube-play" aria-hidden="true"></i><span class="label"></span> YouTube  </a>
# <a href="https://www.instagram.com/JeshuaNomics/"><i class="fa fa-instagram" aria-hidden="true"></i><span class="label"></span> Instagram  </a>
# <a href="https://www.datascience.jeshuanomics.com/"><i class="fa fa-check" aria-hidden="true"></i><span class="label"></span> DataScience </a>
# </center><br><br>

# # Array Processing

# In[1]:


import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')



# In[2]:


#Set array for one side of grid
points = np.arange(-5,5,0.01)


# In[3]:


#Create the grid
dx,dy=np.meshgrid(points,points)


# In[4]:


#Show what one side looks like
dx


# In[5]:


# Evaluating Function
z = (np.sin(dx) + np.sin(dy))


# In[6]:


#Lets take a look at the z result
z


# In[11]:


#Plot out the 2d array
plt.imshow(z)

#Plot with a colorbar
plt.colorbar()

#Give the plot a title
plt.title("Plot for sin(x)+sin(y)")


# In[15]:


#Lets learn how to use the numpy where

#First the slow way to do things

A = np.array([1,2,3,4])

B= np.array([100,200,300,400])

#Now a boolean array
condition = np.array([True,True,False,False])

#Using a list comprehension
answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]

#Show the answer
answer

#Problems include speed issues and multi-dimensional array issues


# In[17]:


#Now using numpy.where

answer2 = np.where(condition,A,B)

#Show
answer2


# In[22]:


#Can use np.where  on 2d for manipulation

from numpy.random import randn

arr = randn(5,5)

#Show arr
arr


# In[24]:


# Where array is less than zero, make that value zero, otherwise leave it as the array value
np.where(arr < 0,0,arr)


# In[43]:


#Other Statistical Processing
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr


# In[42]:


#SUM
arr.sum()


# In[37]:


#Can also do along an axis (we shold expect a 3 diff between the columns)
arr.sum(0)


# In[38]:


#Mean
arr.mean()


# In[39]:


#Standard Deviation
arr.std()


# In[40]:


#Variance
arr.var()


# In[44]:


#Also any and all for processing boolean arrays

bool_arr = np.array([True,False,True])

#For any True
bool_arr.any()


# In[45]:


# For all True
bool_arr.all()


# In[52]:


# Finally sort array

#Create a random array
arr = randn(5)
#show
arr


# In[54]:


#Sort it
arr.sort()
#show
arr


# In[55]:


#Lets learn about unique
countries = np.array(['France', 'Germany', 'USA', 'Russia','USA','Mexico','Germany'])

np.unique(countries)


# In[58]:


# in1d test values in one array
np.in1d(['France','USA','Sweden'],countries)


# In[ ]:




