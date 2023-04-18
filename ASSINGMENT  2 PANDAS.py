#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import numpy as np
import urllib.request


# In[2]:


url = urllib.request.urlopen('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user')


# In[3]:


df = pd.read_csv(url,sep='|',index_col='user_id')
df


#  # See First 10 and last 10 entries

# In[4]:


print("*** First 10 Record ***\n")
print(df.head(10))
print()
print("*** Last 10 Record ***\n")
print(df.tail(10))


# # What is the number of observations in the dataset?

# In[5]:


print(f"Number of Overvation in dataset is :- {len(df.iloc[::,0])}")


# # What is the Number of Column in the dataset?

# In[6]:


print(f" Number of columne in dataset is :-  {len(data.iloc[0])}")


# # Print the Name of All Column

# In[7]:


df.columns


# # How is the Dataset Indexed?

# In[8]:


df.index


# # What is the data type of Each Column?

# In[9]:


df.dtypes


# # Print only occupaction Column

# In[10]:


df['occupation']


# # How Differents Types of Occupaction in Dataset?

# In[11]:


print(f"Types of Occupation :- {len(df['occupation'].unique())}")


# # Dataframe info

# In[12]:


df.info()


# # Sumerize the occupaction Column

# In[13]:


df['occupation'].value_counts()


# # What is the Mean Age of User?

# In[14]:


df['age'].mean()


# # What is the age with least occurrence?

# In[15]:


df['age'].value_counts().idxmin()


# In[ ]:




