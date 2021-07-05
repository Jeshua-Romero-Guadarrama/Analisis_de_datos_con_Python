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

# # Indexing Arrays

# In[11]:


import numpy as np


# In[12]:


#Creating sample array
arr = np.arange(0,11)


# In[6]:


#Show
arr


# In[7]:


#Get a value at an index
arr[8]


# In[9]:


#Get values in a range
arr[1:5]


# In[10]:


#Get values in a range
arr[0:5]


# In[16]:


#Setting a value with index range (Broadcasting)
arr[0:5]=100

#Show
arr


# In[31]:


# Reset array, we'll see why i had to reset in  a moment
arr = np.arange(0,11)

#Show
arr


# In[32]:


#Important notes on Slices
slice_of_arr = arr[0:6]

#Show slice
slice_of_arr



# In[33]:


#Change Slice
slice_of_arr[:]=99

#Show Slice again
slice_of_arr


# In[34]:


# Now note the changes also occur in our original array!
arr

# Data is not copied, it's a view of the original array! This avoids memory problems!


# In[43]:


#To get a copy, need to be explicit
arr_copy = arr.copy()

arr_copy


# In[38]:


# Indexing a 2D array

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

#Show
arr_2d


# In[39]:


#Indexing row
arr_2d[1]


# In[40]:


# Format is arr_2d[row][col] or arr_2d[row,col]

# Getting individual element value
arr_2d[1][0]



# In[41]:


# Getting individual element value
arr_2d[1,0]


# In[45]:


# 2D array slicing

#Shape (2,2) from top right corner
arr_2d[:2,1:]


# In[46]:


#Shape bottom row
arr_2d[2]


# In[47]:


#Shape bottom row
arr_2d[2,:]


# In[66]:


# Fancy Indexing

#Set up matrix
arr2d = np.zeros((10,10))


# In[68]:


#Length of array
arr_length = arr2d.shape[1]


# In[70]:


#Set up array

for i in range(arr_length):
    arr2d[i] = i
    
arr2d


# In[71]:


#Fancy indexing allows the following
arr2d[[2,4,6,8]]


# In[72]:


#Allows in any order
arr2d[[6,4,2,7]]


# In[ ]:




