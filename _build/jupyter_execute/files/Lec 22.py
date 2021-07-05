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

# # Summary Statistics

# In[1]:


#Now we'll learn about pandas built-in methods of summarizing data founr in DataFrames
import numpy as np
from pandas import Series,DataFrame
import pandas as pd


# In[3]:


#Let's create a dataframe to work with
arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1 = DataFrame(arr,index=['A','B'],columns = ['One','Two','Three'])

#Show
dframe1


# In[4]:


#Let's see the sum() method in action
dframe1.sum()


# In[5]:


#Notice how it ignores NaN values


# In[6]:


#We can also over rows instead of columns
dframe1.sum(axis=1)


# In[7]:


#Can also grab min and max values of dataframe
dframe1.min()


# In[8]:


#As well as there index
dframe1.idxmin()


# In[9]:


#Same deal with max, just replace min for max


# In[10]:


#Show
dframe1


# In[11]:


#Can also do an accumulation sum
dframe1.cumsum()


# In[12]:


#A very useful feature is describe, which provides summary statistics
dframe1.describe()


# In[13]:


# We can also get information on correlation and covariance

#For more info on correlation and covariance, check out the videos below!


# In[14]:


from IPython.display import YouTubeVideo
# For more information about Covariaance and Correlation
# Check out these great videos!
# Video credit: Brandon Foltz.

#CoVariance
YouTubeVideo('xGbpuFNR1ME')


# In[15]:


#Correlation
YouTubeVideo('4EXNedimDMs')


# In[16]:


#Now lets check correlation and covariance on some stock prices!

#Pandas can get info off the web
import pandas.io.data as pdweb

#Set datetime for date input
import datetime

#Get the closing prices

prices = pdweb.get_data_yahoo(['CVX','XOM','BP'], 
                               start=datetime.datetime(2010, 1, 1), 
                               end=datetime.datetime(2013, 1, 1))['Adj Close']
#Show preview
prices.head()


# In[17]:


#Now lets get the volume trades

volume = pdweb.get_data_yahoo(['CVX','XOM','BP'], 
                               start=datetime.datetime(2010, 1, 1), 
                               end=datetime.datetime(2013, 1, 1))['Volume']

#Show preview
volume.head()


# In[18]:


#Lets get the return
rets = prices.pct_change()


# In[23]:


#Get the correlation of the stocks
corr = rets.corr


# In[24]:


#Lets see the prices over time to get a very rough idea of the correlation between the stock prices
prices.plot()


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#As expected pretty strong correlations with eachother
sns.heatmap(rets.corr())

#We'll learn much more about seaborn later!


# In[2]:


# We can also check for unique values and their counts 

#For example
ser1 = Series(['w','w','x', 'y', 'z' ,'w' ,'w' ,'x' ,'x' ,'y' ,'a' ,'z' ])

#Show
ser1


# In[3]:


#Grab the unique values
ser1.unique()


# In[4]:


#Now get the count of the unique values
ser1.value_counts()


# In[ ]:


#Next we'll learn how to best deal with missing data!

