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

# # Aggregation

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[6]:


# Data Agrregation consists of operations that result in a scalar (e.g. mean(),sum(),count(), etc)

#Let's get a csv data set to play with
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'


# Save thewinquality.csv file in the same folder as your ipython notebooks, note the delimiter used ;
dframe_wine = pd.read_csv('winequality_red.csv',sep=';')


# In[7]:


# Let's get a preview
dframe_wine.head()


# In[8]:


# How about we find out the average alcohol content for the wine
dframe_wine['alcohol'].mean()


# In[25]:


# That was an example of an aggregate, how about we make our own?
def max_to_min(arr):
    return arr.max() - arr.min()

# Let's group the wines by "quality"
wino = dframe_wine.groupby('quality')

# Show
wino.describe()


# In[22]:


# We can now apply our own aggregate function, this function takes the max value of the col and subtracts the min value of the col
wino.agg(max_to_min)


# In[26]:


# We can also pass string methods through aggregate
wino.agg('mean')


# In[27]:


# Let's go back to the original dframe
dframe_wine.head()


# In[28]:


# Let's adda  quality to alcohol content ratio
dframe_wine['qual/alc ratio'] = dframe_wine['quality']/dframe_wine['alcohol']


# In[29]:


# Show
dframe_wine.head()


# In[32]:


# WE can also use pivot tables instead of groupby

# Pivot table of quality
dframe_wine.pivot_table(index=['quality'])


# In[38]:


get_ipython().run_line_magic('matplotlib', 'inline')
dframe_wine.plot(kind='scatter',x='quality',y='alcohol')


# We can see that the data is probably better fit for a box plot for a more concise view of the data
# See if you can figure how to get a boxplot using the pandas documentation and what you have learned so far
# 
# Don't worry if you can't quite figure it out just yet, the next section will cover all sorts of data visualizations!

# In[ ]:




