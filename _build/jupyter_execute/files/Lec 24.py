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

# # Index Hierarchy

# In[1]:


import numpy as np
from pandas import Series,DataFrame
import pandas as pd

from numpy.random import randn


# In[11]:


#Now we'll learn about Index Hierarchy

#pandas allows you to have multiple index levels, which is very clear with this example:

ser = Series(np.random.randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])


# In[12]:


#Show Series with multiple index levels
ser


# In[14]:


# We can check the multiple levels
ser.index


# In[15]:


#Now we can sleect specific subsets
ser[1]


# In[16]:


# We can also select from an internal index level
ser[:,'a']


# In[19]:


# We can also create Data Frames from Series with multiple levels
dframe = ser.unstack()

#Show
dframe


# In[20]:


#Can also reverse
dframe.unstack()


# In[28]:


# We can also apply multiple level indexing to DataFrames
dframe2 = DataFrame(np.arange(16).reshape(4,4),
                    index=[['a','a','b','b'],[1,2,1,2]],
                    columns=[['NY','NY','LA','SF'],['cold','hot','hot','cold']])
                                                   
dframe2                                                


# In[31]:


# We can also give these index levels names

#Name the index levels
dframe2.index.names = ['INDEX_1','INDEX_2']

#Name the column levels
dframe2.columns.names = ['Cities','Temp']

dframe2


# In[33]:


# We can also interchange level orders (note the axis=1 for columns)
dframe2.swaplevel('Cities','Temp',axis=1)


# In[34]:


#We can also sort levels
dframe2.sortlevel(1)


# In[35]:


#Note the change in sorting, now the Dframe index is sorted by the INDEX_2


# In[37]:


#We can also perform operations on particular levels
dframe2.sum(level='Temp',axis=1)


# In[38]:


#Thats the end of this section! Next up, Section 5: Working with Data Part 1 !!!


# In[ ]:




