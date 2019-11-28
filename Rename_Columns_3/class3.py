# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:41:53 2019

@author: RAJESH
"""

#Loading required packages 
import pandas as pd
import numpy as np
#............,.........

#Loading dataset into dataframe
dataset = pd.read_csv("Data.csv")
#......................


####Lets play with column names
#Finding column names
dataset.columns
#Below is the way to alter coloumn names
dataset = dataset.rename(columns = {'Salary':'Income'})
#We can change mutliple columns at time
dataset = dataset.rename(columns = {'Income':'Salary','Age':'XXX'})
#Back to native column
dataset = dataset.rename(columns = {'XXX':'Age'})
#.......................

#Replacing disired value into the columns 
#Simple replacing Null value of Salary with 50 thousands. This is direct statement
dataset['Salary'] = dataset['Salary'].replace(np.NaN,500000)
#Replacing with the strategy of mean
dataset['Age'] = dataset['Age'].replace(np.NaN,np.round(np.mean(dataset['Age']),0))
#.......................


#Storing value at particular cell in the data frame       
# -------> 1 .at  -> based on the col names and row names(index names)
#          2 .iat -> based on the  DataFrame by integer location only
dataset.iat[6,2] = 40

dataset.at[1,'Place'] = 'India'

dataset = dataset.set_index(dataset['Place'])

dataset.at['Spain','Age'] = 10
#..........................



