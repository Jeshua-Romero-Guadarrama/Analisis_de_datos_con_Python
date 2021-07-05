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

# # Splitting, Applying and Combining

# In[1]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


# Let's grab the wine data again
dframe_wine = pd.read_csv('winequality_red.csv',sep=';')

#Preview
dframe_wine.head()


#  What if we wanted to know the highest alcohol content for each quality range?
#  
#  We can use groupby mechanics to split-apply-combine

# In[4]:


# Create a function that assigns a rank to each wine based on alcohol content, with 1 being the highest alcohol content
def ranker(df):
    df['alc_content_rank'] = np.arange(len(df)) + 1
    return df


# In[8]:


# Now sort the dframe by alcohol in ascending order
dframe_wine.sort('alcohol',ascending=False,inplace=True)

# Now we'll group by quality and apply our ranking function
dframe_wine = dframe_wine.groupby('quality').apply(ranker)


# In[9]:


#Preview
dframe_wine.head()


# In[13]:


# Now finally we can just call for the dframe where the alc_content_rank == 1

# Get the numebr of quality counts
num_of_qual = dframe_wine['quality'].value_counts()

#Show
num_of_qual


# In[15]:


# Now we'll show the combined info for teh wines that had the highest alcohol content for their respective rank!
dframe_wine[dframe_wine.alc_content_rank == 1].head(len(num_of_qual))


# In[ ]:


# Awesome! Ask yourself if there are any trends you would like to find in this data?
# Is there a relationship between wine ranking and alcohol content?

