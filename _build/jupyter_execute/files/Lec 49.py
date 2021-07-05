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

# # Kernel Density Estimation Plots

# In[30]:


# The normal imports
import numpy as np
from numpy.random import randn
import pandas as pd

# Import the stats library from numpy
from scipy import stats

# These are the plotting modules adn libraries we'll use:
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Command so that plots appear in the iPython Notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# First we'll learn how to understand and make a KDE plot manually, and then we'll see how to do it quickly with seaborn!

# In[31]:


# Let's start off with a carpet/rug plot
# A rug plot simpot puts ticks wherever a value occured

#Create dataset
dataset = randn(25)
#Create rugplot
sns.rugplot(dataset)
#Set y-axis limit
plt.ylim(0,1)


# In[32]:


# Plot a histogram on top of 
plt.hist(dataset,alpha=0.3)
sns.rugplot(dataset)


# The histogram sets up 10 bins and then just count how many ticks appeared in each bin, setting the height of each bar

# The kernel density plot will represent each tick mark with a gaussian basis function.
# Let's see how we would do this manually

# In[39]:


# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)


# In[55]:


# To get the kde plot we can sum these basis functions.



# Plot the sum of the basis function
sum_of_kde = np.sum(kernels,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")


# In[58]:


# Now we can see how to do it in one step with seaborn! Awesome!
sns.kdeplot(dataset)


# In[73]:


# We can adjust the bandwidth of the sns kde to make the kde plot more or less sensitive to high frequency

# Rugplot
sns.rugplot(dataset,color='black')

# Plot various bandwidths
for bw in np.arange(0.5,2,0.25):
    sns.kdeplot(dataset,bw=bw,lw=1.8,label=bw)


# In[75]:


# We can also choose different kernels

kernel_options = ["biw", "cos", "epa", "gau", "tri", "triw"]

# More info on types
url = 'http://en.wikipedia.org/wiki/Kernel_(statistics)'

# Use label to set legend
for kern in kernel_options:
    sns.kdeplot(dataset,kernel=kern,label=kern)


# In[79]:


# We can also shade if desired
for kern in kernel_options:
    sns.kdeplot(dataset,kernel=kern,label=kern,shade=True,alpha=0.5)


# In[76]:


# For vertical axis, use the vertical keyword
sns.kdeplot(dataset,vertical=True)


# In[81]:


# Finally we can also use kde plot to create a cumulative distribution function (CDF) of the data

# URL for info on CDF
url = 'http://en.wikipedia.org/wiki/Cumulative_distribution_function'

sns.kdeplot(dataset,cumulative=True)


# ### Multivariate Density Estimation using kdeplot

# We can also use kdeplot for multidimensional data. Lets see how it works!

# In[88]:


# Let's create a new dataset

# Mean center of data
mean = [0,0]

# Diagonal covariance
cov = [[1,0],[0,100]]

# Create dataset using numpy
dataset2 = np.random.multivariate_normal(mean,cov,1000)

# Bring back our old friend pandas
dframe = pd.DataFrame(dataset2,columns=['X','Y'])

# Plot our dataframe
sns.kdeplot(dframe)


# In[89]:


# We could have also passed two vectors seperately, and shade
sns.kdeplot(dframe.X,dframe.Y,shade=True)


# In[90]:


# Can specify a particualr bandwidth
ns.kdeplot(dframe,bw=1)


# In[92]:


# Or just use silverman again
sns.kdeplot(dframe,bw='silverman')


# In[94]:


# We can also create a kde joint plot, simliar to the hexbin plots we saw before

sns.jointplot('X','Y',dframe,kind='kde')


# In[97]:


# Next up: Combingign plot styles using distplot!


# In[ ]:




