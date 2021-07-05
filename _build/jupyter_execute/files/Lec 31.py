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

# # Concatenate

# In[2]:


# Now we'll learn about concatenating along an axis
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[3]:


# First in just Numpy


# In[4]:


# Create a matrix 
arr1 = np.arange(9).reshape((3,3))


# In[5]:


# Show
arr1


# In[6]:


# Concatenate along axis 1
np.concatenate([arr1,arr1],axis=1)


# In[7]:


# Let's see other axis options
np.concatenate([arr1,arr1],axis=0)


# In[8]:


# Now let's see how this works in pandas


# In[9]:


# Lets create two Series with no overlap
ser1 =  Series([0,1,2],index=['T','U','V'])

ser2 = Series([3,4],index=['X','Y'])

#Now let use concat (default is axis=0)
pd.concat([ser1,ser2])


# In[10]:


# Now passing along another axis will produce a DataFrame
pd.concat([ser1,ser2],axis=1)


# In[17]:


# We can specify which specific axes to be used
pd.concat([ser1,ser2],axis=1,join_axes=[['U','V','Y']])


# In[11]:


# Lets say we wanted to add markers.keys to the concatenation result

# WE can do this with a hierarchical index
pd.concat([ser1,ser2],keys=['cat1','cat2'])


# In[12]:


# Along the axis=1 then these Keys become column headers
pd.concat([ser1,ser2],axis=1,keys=['cat1','cat2'])


# In[14]:


#Lastly, everything works similarly in DataFrames

dframe1 = DataFrame(np.random.randn(4,3), columns=['X', 'Y', 'Z'])
dframe2 = DataFrame(np.random.randn(3, 3), columns=['Y', 'Q', 'X'])


# In[16]:


#Concat on DataFrame
pd.concat([dframe1,dframe2])


# In[17]:


#If we dont care about the index info and just awnt to make a complete DataFrame, just use ignore_index
pd.concat([dframe1,dframe2],ignore_index=True)


# In[18]:


#For more info in documentation:
url='http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html'


# In[ ]:


#Next up: More on Combining DataFrames with Overlapping Indexes!

