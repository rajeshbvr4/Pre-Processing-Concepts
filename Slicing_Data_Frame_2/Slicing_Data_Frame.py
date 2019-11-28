# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:09:32 2019

This will explains the Splitting data using loc and iloc concepts

@author: RAJESH
"""

#Loading packages 
import pandas as pd


#loading dataset
dataset = pd.read_csv('Data.csv')
#........


#Spllitting data set using iloc
# Rows - 2,3 and Coloumns- all
dataset.iloc[2:4]
# Rows - 1,2,3 and Coloumns- 2,3
dataset.iloc[1:4,2:4]
# Rows - all and Coloumns - 1,3 (Specific coloumns extraction)
dataset.iloc[:, [1,3]]

#Rows - All, and Columns -  last one
dataset.iloc[:,-1].values

#Rows - All, and Columns - all without last one
dataset.iloc[:,:-1].values

#Rows - All, and Columns - first one
dataset.iloc[:, [1]].values

#Rows - All, and Columns - 1 and 2
dataset.iloc[:,[1,2]]


#Extracting 1st row with 1st column
dataset.iloc[1][1]

#...............


#Splitting data using loc#
#Check Indexing of dataset. Set any coloumn if not
dataset = dataset.set_index(dataset['Country'])
#Extract the data which is based on indexing
# Rows - 'Germany data rows' and Coloumns = ALl
dataset.loc['Germany', :]
#Rows - 'France' and Coloumns - 'Salary', 'Purchased
dataset.loc['France',['Salary','Purchased']]
#Rows - 'France' , Germany and Coloumns - 'Salary', 'Purchased
dataset.loc[['France','Germany'],['Salary','Purchased']]
#................




#Setting index makes you accessing data label wise if index as numbering 
dataset = dataset.set_index(dataset['Country'])
#.............

#Based on the condition 
#Single condition
dataset[dataset['Country'] == 'France']
#Mutiple condition 
dataset[(dataset['Country'] == 'France') & (dataset['Salary'] > 75000)]

z = dataset.iloc[6][1]

x = str(dataset.iloc[5][0:2])



#.............
