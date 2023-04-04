#!/usr/bin/env python
# coding: utf-8

# ## COLUMN OPERATIONS

# ## The World's Biggest Public Companies 2021
# 
# ### Since 2003, Forbes’ Global 2000 list has measured the world’s largest public companies in terms of four equally weighted metrics: assets, market value, sales and profits.
# 
# #### You can find the biggest 500 companies in this data.

# In[1]:


import pandas as pd


# #### pandas library imported as pd for data exploration.

# In[17]:


data=pd.read_csv("C://Users//indhu//OneDrive//Documents//PYTHON WORKINGS//The Worlds Biggest Public Companies.csv")


# #### The Worlds Biggest Public Companies dataset is read from the location.

# In[18]:


data


# #### This dataset is downloaded from kaggle.com

# In[4]:


data['Real_Salesprice']=data['Sales(in Billion)']-data['Profit(in Billion)']


# In[5]:


data


# #### A new variable named Real_Salesprice is added to the dataset.

# In[6]:


data.rename(columns={'Real_Salesprice':'Real_Salesvalue'})


# #### Variable name Real_Salesprice is replaced with Real_Salesvalue.

# In[7]:


data.rename(columns={'Sales(in Billion)':'Sales','Profit(in Billion)':'Profit','Assets(in Billion)':'Assets','Market Value(in Billion)':'Market Value'})


# #### 4 variable names are replaced.

# In[8]:


data.drop(['Real_Salesprice'],axis=1)


# #### Variable named "Real_Salesprice" is removed from the dataset.

# In[9]:


data.drop(['Real_Salesprice','Market Value(in Billion)'],axis=1)


# #### More than 1 variable is removed from the dataset.

# In[10]:


data.columns=[col.upper()for col in data.columns]


# In[11]:


data.columns


# #### Variables are converted to Upper case.

# In[15]:


data.columns1=[col.lower()for col in data.columns]


# In[16]:


data.columns1


# #### Variables are converted to lower case.

# In[19]:


data.sort_values(by='Profit(in Billion)',ascending=True)


# #### Dataset is sorted based on Profit.

# In[20]:


data.sort_values(by=['Sales(in Billion)','Profit(in Billion)'],ascending=[True,True])


# #### Dataset is sorted based on Sales and Profit.

# In[21]:


data.groupby('Rank').count()


# #### The dataset is grouped and counted based on Rank.

# In[22]:


print(data['Profit(in Billion)'].isnull().sum())


# #### The dataset is checked for null values. There is no null values in the dataset.

# In[23]:


print(len(data.columns.values))


# #### 7 variables available in the dataset.

# In[24]:


print(data.columns.values)


# #### The columns of the dataset are listed.
