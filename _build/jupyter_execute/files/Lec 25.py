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

# # Reading and Writing Text Files

# In[2]:


import numpy as np
from pandas import Series,DataFrame
import pandas as pd


# In[3]:


# Can open csv files as a dataframe
dframe = pd.read_csv('lec25.csv')

#Show
dframe


# In[4]:


# Can also use read_table with ',' as a delimiter
dframe = pd.read_table('lec25.csv',sep=',')

#Show
dframe


# In[5]:


dframe


# In[6]:


#If we dont want the header to be the first row
dframe = pd.read_csv('lec25.csv',header=None)

#Show
dframe


# In[7]:


# We can also indicate a particular number of rows to be read
pd.read_csv('lec25.csv',header=None,nrows=2)


# In[8]:


# Let's see dframe again
dframe


# In[10]:


# Now let's see how we can write DataFrames out to text files
dframe.to_csv('mytextdata_out.csv')

#You'll see this file where you're ipython Notebooks are saved (Usually under my documents)


# In[14]:


#  We can also use other delimiters

#we'll import sys to see the output
import sys 

#Use sys.stdout to see the output directly and not save it
dframe.to_csv(sys.stdout,sep='_')


# In[15]:


# Just to make sure we understand the delimiter
dframe.to_csv(sys.stdout,sep='?')


# In[17]:


#We can also choose to write only a specific subset of columns
dframe.to_csv(sys.stdout,columns=[0,1,2])


# In[18]:


#You should also check out pythons built-in csv reader and writer for more info:
# https://docs.python.org/2/library/csv.html


# In[ ]:


#Next we'll learn about reading JSON data!

