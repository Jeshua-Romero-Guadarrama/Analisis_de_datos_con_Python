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

# # DataFrames

# In[1]:


import numpy as np
from pandas import Series, DataFrame
import pandas as pd


# In[2]:


#Now we'll learn DataFrames

#Let's get some data to play with. How about the NFL?
import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)


# In[3]:


#Copy and read to get data
nfl_frame = pd.read_clipboard()


# In[5]:


#Show
nfl_frame


# In[6]:


# We can grab the oclumn names with .columns
nfl_frame.columns


# In[22]:


#Lets see some specific data columns
DataFrame(nfl_frame,columns=['Team','First Season','Total Games'])


# In[11]:


#What happens if we ask for a column that doesn't exist?
DataFrame(nfl_frame,columns=['Team','First Season','Total Games','Stadium'])


# In[13]:


# Call columns
nfl_frame.columns


# In[18]:


#We can retrieve individual columns
nfl_frame.Team


# In[19]:


# Or try this method for multiple word columns
nfl_frame['Total Games']


# In[25]:


#We can retrieve rows through indexing
nfl_frame.ix[3]


# In[26]:


#We can also assign value sto entire columns
nfl_frame['Stadium']="Levi's Stadium" #Careful with the ' here


# In[28]:


nfl_frame


# In[9]:


#Putting numbers for stadiums
nfl_frame["Stadium"] = np.arange(5)

#Show
nfl_frame


# In[10]:


# Call columns
nfl_frame.columns


# In[14]:


#Adding a Series to a DataFrame
stadiums = Series(["Levi's Stadium","AT&T Stadium"],index=[4,0])


# In[15]:


#Now input into the nfl DataFrame
nfl_frame['Stadium']=stadiums

#Show
nfl_frame


# In[16]:


#We can also delete columns
del nfl_frame['Stadium']

nfl_frame


# In[17]:


#DataFrames can be constructed many ways. Another way is from a dictionary of equal length lists
data = {'City':['SF','LA','NYC'],
        'Population':[837000,3880000,8400000]}

city_frame = DataFrame(data)

#Show
city_frame


# In[40]:


#For full list of ways to create DataFrames from various sources go to teh documentation for pandas:
website = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html'
webbrowser.open(website)


# In[ ]:




