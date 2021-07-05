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

# # Rename Index

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[13]:


# Making a DataFrame
dframe= DataFrame(np.arange(12).reshape((3, 4)),
                 index=['NY', 'LA', 'SF'],
                 columns=['A', 'B', 'C', 'D'])

#Show
dframe


# In[14]:


# Just like a Series, axis indexes can also use map

#Let's use map to lowercase the city initials
dframe.index.map(str.lower)


# In[25]:


# If you want to assign this to the actual index, you can use index
dframe.index = dframe.index.map(str.lower)
#Show
dframe


# In[28]:


# Use rename if you want to create a transformed version withour modifying the original!

#str.title will capitalize the first letter, lowercasing the columns
dframe.rename(index=str.title, columns=str.lower)


# In[34]:


# We can also use rename to insert dictionaries providing new values for indexes or columns!
dframe.rename(index={'ny': 'NEW YORK'},
            columns={'A': 'ALPHA'})


# In[38]:


# If you would like to actually edit the data set in place, set inplace=True
dframe.rename(index={'ny': 'NEW YORK'}, inplace=True)
dframe


# In[1]:


#Up next: Binning!


# In[ ]:




