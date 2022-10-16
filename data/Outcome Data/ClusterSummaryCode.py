#!/usr/bin/env python
# coding: utf-8

# ## SDOH Atlas Cluster Summary Statistics
# Code to pull summary statistics for 8 Clusters
# Exports 8 excel sheets for each cluster with data and summary stats
# 

# In[29]:


#import libraries 
 
import pandas as pd
import numpy as np
import openpyxl 
from openpyxl.writer.excel import ExcelWriter


# In[39]:


#read in data & get summary info

df = pd.read_csv ('SDOH2022.csv')
#df.head()    #shows head and first five rows
#df.columns  #read column headings


# In[21]:


#create variable for each cluster
cl1 = df[df["CL"] == 1]
cl2 = df[df["CL"] == 2]
cl3 = df[df["CL"] == 3]
cl4 = df[df["CL"] == 4]
cl5 = df[df["CL"] == 5]
cl6 = df[df["CL"] == 6]
cl7 = df[df["CL"] == 7]
cl8 = df[df["CL"] == 8]

clusters = [cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8]


# In[41]:


#definition to export excel with two sheets
#parameter 1 "data" = data for each cluster
#parameter 2 "stats" = summary stats for each cluster
#parameter 3 "num" = number of cluster for naming purposes

def createExcel(data,stats,num):
    name = 'cluster' + str(num) + '.xlsx'
    with pd.ExcelWriter(name) as writer:  
        data.to_excel(writer, sheet_name='data')
        stats.to_excel(writer, sheet_name='sumstats')


# In[38]:


#Loop through each cluster and use createExcel function to create excel files for each cluster

counter = 1
for i in clusters: 
    num = counter
    sumStats = i.describe()
    createExcel(i,sumStats,num)
    counter += 1

