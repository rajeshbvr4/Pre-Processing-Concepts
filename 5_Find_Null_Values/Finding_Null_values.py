# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:46:21 2019

HOW TO FIND NULL VALUES IN THE DATA SET.
1. isnull() -> True if it is Null value 
2. notnull() -> True if it is Not-Null value

@author: RAJESH
"""

#Loading required packages 
import pandas as pd
#.....................

#Loading dataset into Data Frame #dataset
dataset = pd.read_csv('Data.csv')
#.....................


#what are the coloumns names:
dataset.columns
#.....................

#What is the difference between isnull and notnull:

dataset['Age'].isnull()
dataset['Age'].notnull()


#How many null values in the data by eacg column
print(dataset.isnull())
#Finding total null values  by each column
print(dataset.isnull().sum())
#Finding total null values  by whole dataset
print(dataset.isnull().sum().sum())
#.........................



dataset['Salary'].isnull().sum()

dataset['Salary'].notnull().sum()








