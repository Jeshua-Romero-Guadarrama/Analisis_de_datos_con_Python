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

# # Reindexing

# In[1]:


#Now we'll elarn about reindexing


# In[23]:


import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn


# In[4]:


#Lets create a new series
ser1 = Series([1,2,3,4],index=['A','B','C','D'])


# In[5]:


#Show
ser1


# In[6]:


#Call reindex to rearrange the data to a new index
ser2 = ser1.reindex(['A','B','C','D','E','F'])


# In[7]:


#Show
ser2


# In[13]:


# We can alos fill in values for new indexes
ser2.reindex(['A','B','C','D','E','F','G'],fill_value=0)


# In[15]:


#Using a particular method for filling values
ser3 = Series(['USA','Mexico','Canada'],index=[0,5,10])

#Show
ser3


# In[20]:


#Can use a forward fill for interploating values vetween indices 
ser3.reindex(range(15),method='ffill')


# In[29]:


#Reindexing rows, columns or both

#Lets make a datafram ewith some random values
dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])

#Show
dframe


# In[37]:


#Notice we forgot 'C' , lets reindex it into dframe
dframe2 = dframe.reindex(['A','B','C','D','E','F'])


# In[38]:


#Can also explicitly reindex columns
new_columns = ['col1','col2','col3','col4','col5','col6']

dframe2.reindex(columns=new_columns)


# In[40]:


#Reindex quickly using the label-indexing with ix (we'll see this more in the future)

#Show original
dframe


# In[41]:


dframe.ix[['A','B','C','D','E','F'],new_columns]


# In[ ]:




