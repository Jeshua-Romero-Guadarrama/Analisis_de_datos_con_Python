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

# # Groupby on Dict and Series

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#let's learn how to use dict or series with groupby


# In[19]:


# Let's make a Dframe

animals = DataFrame(np.arange(16).reshape(4, 4),
                   columns=['W', 'X', 'Y', 'Z'],
                   index=['Dog', 'Cat', 'Bird', 'Mouse'])

#Now lets add some NAN values
animals.ix[1:2, ['W', 'Y']] = np.nan 

#Show
animals


# In[20]:


# Now let's say I had a dictionary with ebhavior values in it
behavior_map = {'W': 'good', 'X': 'bad', 'Y': 'good','Z': 'bad'}


# In[21]:


# Now we can groupby using that mapping
animal_col = animals.groupby(behavior_map, axis=1)

# Show the sum accroding to the groupby with the mapping
animal_col.sum()

# For example [dog][good] = [dog][Y]+[dog][W]


# In[22]:


# Now let's try it with a Series
behav_series = Series(behavior_map)

#Show
behav_series


# In[23]:


# Now let's groupby the Series

animals.groupby(behav_series, axis=1).count()


# In[26]:


# We can also groupby with functions!

#Show our dframe again
animals


# In[25]:


# Lets assume we wanted to group by the length of the animal names, we can pass the len function into groupby!

# Show
animals.groupby(len).sum()

#Note the index is now number of letters in the animal name


# In[29]:


# We can also mix functions with arrays,dicts, and Series for groupby methods

# Set a list for keys
keys = ['A', 'B', 'A', 'B']

# Now groupby length of name and the keys to show max values
animals.groupby([len, keys]).max()


# In[36]:


# We can also use groupby with hierarchaly index levels

#Create a hierarchal column index
hier_col = pd.MultiIndex.from_arrays([['NY','NY','NY','SF','SF'],[1,2,3,1,2]],names=['City','sub_value'])

# Create a dframe with hierarchal index
dframe_hr = DataFrame(np.arange(25).reshape(5,5),columns=hier_col)

#Multiply values by 100 for clarity
dframe_hr = dframe_hr*100

#Show
dframe_hr


# In[ ]:


#Up next: Data Aggregation!!

