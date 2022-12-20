#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


Transactions = pd.read_excel("KPMG_VI_New_raw_data_update_final.xlsx", "Transactions", header=1)


# In[4]:


display(Transactions.head())
display(Transactions.tail())


# In[5]:


print("Transactions shape (Rows, Columns):", Transactions.shape)


# In[6]:


Transactions.info()


# In[7]:


Transactions.columns


# In[8]:


Transactions.count()


# In[9]:


Transactions.isnull().sum()


# In[10]:


Transactions.duplicated().sum()


# In[11]:


Transactions['transaction_id'].nunique()


# In[12]:


Transactions['transaction_id'].value_counts().sort_index(ascending=True)


# In[13]:


Transactions['product_id'].nunique()


# In[14]:


Transactions['product_id'].value_counts().sort_index(ascending=True)


# In[ ]:





# In[16]:


NewCustomerList = pd.read_excel("KPMG_VI_New_raw_data_update_final.xlsx", "NewCustomerList", header=1)
display(NewCustomerList.head())
display(NewCustomerList.tail())


# In[17]:


print("NewCustomerList shape (Rows, Columns):", NewCustomerList.shape)


# In[18]:


NewCustomerList.info()


# In[19]:


NewCustomerList.columns


# In[20]:


NewCustomerList.count()


# In[21]:


NewCustomerList.isnull().sum()


# In[22]:


CustomerDemographic = pd.read_excel("KPMG_VI_New_raw_data_update_final.xlsx", "CustomerDemographic", header=1)
display(CustomerDemographic.head())
display(CustomerDemographic.tail())


# In[23]:


print("Transactions shape (Rows, Columns):", CustomerDemographic.shape)


# In[24]:


CustomerDemographic.info()


# In[25]:


CustomerDemographic.columns


# In[26]:


CustomerDemographic.count()


# In[27]:


CustomerDemographic.isnull().sum()


# In[28]:


CustomerDemographic['customer_id'].nunique()


# In[29]:


CustomerDemographic['customer_id'].value_counts().sort_index(ascending=True)


# In[30]:


CustomerDemographic['gender'].unique()


# In[31]:


CustomerDemographic['gender'].nunique()


# In[32]:


CustomerDemographic['gender'].value_counts().sort_index(ascending=True)


# In[33]:


CustomerDemographic['gender'].replace('F', 'Female', inplace=True)
CustomerDemographic['gender'].replace('Femal', 'Female', inplace=True)
CustomerDemographic['gender'].replace('M', 'Male', inplace=True)
CustomerDemographic['gender'].unique()


# In[34]:


CustomerAddress = pd.read_excel("KPMG_VI_New_raw_data_update_final.xlsx", "CustomerAddress", header=1)
display(CustomerAddress.head())
display(CustomerAddress.tail())


# In[35]:


print("Transactions shape (Rows, Columns):", CustomerAddress.shape)


# In[36]:


CustomerAddress.info()


# In[37]:


CustomerAddress.columns


# In[38]:


CustomerAddress.count()


# In[39]:


CustomerAddress.isnull().sum()


# In[ ]:




