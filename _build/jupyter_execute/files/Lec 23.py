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

# # Missing Data

# In[1]:


import numpy as np
from pandas import Series,DataFrame
import pandas as pd


# In[2]:


#Now we'll learn how to deal with missing data, a very common task when analyzing datasets!

data = Series(['one','two', np.nan, 'four'])


# In[3]:


#Show data
data


# In[5]:


#Find the missing values
data.isnull()


# In[7]:


#We can simply drop the NAN 
data.dropna()


# In[14]:


# In a DataFrame we need to be a little more careful!

dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])


# In[15]:


#Show
dframe


# In[16]:


clean_dframe = dframe.dropna()


# In[17]:


#Show
clean_dframe


# In[12]:


#Note all rows where an NA occured was a drop of the entire row


# In[18]:


#We can also specify to only drop rows that are complete missing all data
dframe.dropna(how='all')


# In[22]:


#Or we can specify to drop columns with missing data
dframe.dropna(axis=1)

#This should drop all columns out since every column contains at least 1 NAN


# In[26]:


#We can also threshold teh missing data as well

#For example if we only want rows with at least 3 data points
dframe2 = DataFrame([[1,2,3,np.nan],[2,np.nan,5,6],[np.nan,7,np.nan,9],[1,np.nan,np.nan,np.nan]])

#Show
dframe2


# In[28]:


#Droppin any rows tht dont have at least 2 data points
dframe2.dropna(thresh=2)


# In[29]:


#Dropiing rows without at least 3 data points
dframe2.dropna(thresh=3)


# In[30]:


#We can also fill any NAN
dframe2.fillna(1)


# In[33]:


#Can also fill in diff values for diff columns
dframe2.fillna({0:0,1:1,2:2,3:3})


# In[34]:


#Note that we still have access to the original dframe
dframe2


# In[35]:


#If we want to modify the exsisting object, use inplace
dframe2.fillna(0,inplace=True)


# In[36]:


#Now let's see the dframe
dframe2


# In[ ]:


#Awesome! Next we'll learn about Index Hierarchy

