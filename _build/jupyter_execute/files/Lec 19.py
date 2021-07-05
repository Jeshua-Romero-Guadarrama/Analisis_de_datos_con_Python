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

# # Selecting Entries

# In[1]:


#Now we'll learn about Selecting Entries
import numpy as np
from pandas import Series,DataFrame
import pandas as pd


# In[9]:


#Lets try some Series indexing
ser1 = Series(np.arange(3),index=['A','B','C'])

#multiply all values by 2, to avoid confusion in future
ser1 = 2*ser1

#Show
ser1 


# In[11]:


#Can grab entry by index name
ser1['B']


# In[13]:


#Or grab by index 
ser1[1]


# In[15]:


#Can also grab by index range
ser1[0:3]


# In[16]:


#Or grab range by range of index values
ser1[['A','B','C']]


# In[17]:


#Or grab by logic
ser1[ser1>3]


# In[19]:


#Can also ser using these methods
ser1[ser1>3] = 10

#Show
ser1


# In[20]:


#Now let's see sleection in a DataFrame

dframe = DataFrame(np.arange(25).reshape((5,5)),index=['NYC','LA','SF','DC','Chi'],columns=['A','B','C','D','E'])

#Show
dframe


# In[21]:


#Select by column name
dframe['B']


# In[23]:


#Select by multiple columns
dframe[['B','E']]


# In[24]:


#Can also use boolean
dframe[dframe['C']>8]


# In[25]:


#Can also just shoe a boolean DataFrame
dframe> 10


# In[26]:


#Can alos use ix as previously discussed to label-index
dframe.ix['LA']


# In[28]:


#Another example
dframe.ix[1]


# In[ ]:


#Next we'll learn about data alignment!

