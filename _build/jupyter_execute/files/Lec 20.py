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

# # Data Alignment

# In[1]:


#Now we'll learn about arithmetic between DataFrames with different indexes
import numpy as np
from pandas import Series,DataFrame

import pandas as pd


# In[2]:


#Lets start by making two Series

ser1 = Series([0,1,2],index=['A','B','C'])

#Show
ser1


# In[5]:


#Now second Series 2
ser2 = Series([3,4,5,6],index=['A','B','C','D'])

#Show 
ser2 


# In[6]:


#So what happens when we add these together
ser1 + ser2


# In[7]:


#Note the NaN values are added in automatically


# In[8]:


# Now let's try it with DataFrames!
dframe1 = DataFrame(np.arange(4).reshape(2,2),columns=list('AB'),index=['NYC','LA'])

#Show
dframe1


# In[10]:


#Second DataFrame
dframe2 = DataFrame(np.arange(9).reshape(3,3),columns=list('ADC'),index=['NYC','SF','LA'])

#Show
dframe2


# In[11]:


#What happens when we add them together?

dframe1 + dframe2


# In[13]:


#What if we want to replace the NaN values
# Then we can use .add()

dframe1.add(dframe2,fill_value=0)


# In[14]:


#Now we can see that the values are filled, however there was no SF,B value so that is still NaN


# In[18]:


#Lets learn about operations betwen a Series and a DataFrame


# In[19]:


#Show
dframe2


# In[23]:


#Create a Series from DataFrame's 0 row
ser3 = dframe2.ix[0]

#Show
ser3


# In[24]:


#Now we can use arithmetic operations
dframe2-ser3


# In[ ]:


#Next we'll learn about sorting and ranking!


# In[ ]:





# In[ ]:




