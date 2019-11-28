# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:40:51 2019

@author: RAJESH
"""

#importing packages
import pandas as pd
import numpy as np
#..............


#Loading Dataset
df = pd.DataFrame()

#Add columns
df['Rank'] = [1,2,3,4,5]
df['Name'] = ['Kohli','Smith','Rohit','Warner','Butler']
df['Points'] = [845,831,803,799,784]
#.............

#Add row to the data frame df
new_row = [6,'Roy',765]
new_series = pd.Series(new_row, index=['Rank','Name','Points'])
df = df.append(new_series, ignore_index=True)
#................

#Add one more column 
df['Country'] = ['India','Australia','India','Australia','England','Newziland']
#.............

#Describing the Data frame
df.describe()

#Data frame information
df.info()

#Coloumn Name
df.columns
df.index
#...........


#Display top 5 rowns  and last 5 rowns
df.head()
df.tail()
#.............

#shape of the data frame

df.shape
