#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


#Export Data
rw = pd.read_excel(r"C:\Users\data anylitics\Desktop\exportt.xlsx")


# In[3]:


#rw = rw[['modify_d','phone_number', 'Disposition', 'Lead status']]


# In[4]:


rw.head()


# In[5]:


a = rw.value_counts(['phone_number']) 

x = pd.DataFrame(a)

x = x.rename(columns = {0 : 'Attempts'})


# In[6]:


rw = pd.merge(rw, x, how = "inner", on = "phone_number")

rw.head()


# In[7]:


rw.to_excel(r'C:\Users\data anylitics\Desktop\Akshay\\Report.xlsx')

