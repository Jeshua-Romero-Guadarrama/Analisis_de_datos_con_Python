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

# # Series

# In[15]:


import numpy as np

from pandas import Series,DataFrame
import pandas as pd


# In[16]:


#Lets create a Series (array of data and data labels, its index)

obj = Series([3,6,9,12])

#Show
obj


# In[17]:


#Lets show the values
obj.values


# In[18]:


#Lets show the index
obj.index


# In[21]:


#Now lets create a Series with an index

#WW2 casualties 
ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])

#Show
ww2_cas


# In[22]:


#Now we can use index values to select Series values
ww2_cas['USA']


# In[26]:


#Can also check with array operations

#Check who had casualties greater than 4 million
ww2_cas[ww2_cas>4000000]


# In[27]:


#Can treat Series as ordered dictionary

#Check if USSR is in Series
'USSR' in ww2_cas


# In[31]:


#Can convert Series into Python dictionary
ww2_dict = ww2_cas.to_dict()

#Show
ww2_dict


# In[34]:


#Can convert back into a Series
WW2_Series = Series(ww2_dict)


# In[35]:


#Show
WW2_Series


# In[36]:


#Passing a dictionary the index will have the dict keys in order
countries = ['China','Germany','Japan','USA','USSR','Argentina']


# In[37]:


#Lets redefine a Series
obj2 = Series(ww2_dict,index=countries)


# In[38]:


#Show
obj2


# In[39]:


#We can use isnull and notnull to find missing data
pd.isnull(obj2)

#obj2.isnull() 


# In[40]:


#Same for the opposite
pd.notnull(obj2)

#obj2.notnull()


# In[41]:


#Lets see the ww2 Series again
WW2_Series


# In[42]:


#Lets check our Series with Argentine again
obj2


# In[43]:


#Now we can add and pandas automatically aligns data by index
WW2_Series + obj2


# In[45]:


#We can give Series names
obj2.name = "World War 2 Casualties"


# In[46]:


#Show
obj2


# In[47]:


#We can also name index
obj2.index.name = 'Countries'


# In[48]:


#Show
obj2


# In[49]:


#Next we'll learn DataFrames!


# In[ ]:




