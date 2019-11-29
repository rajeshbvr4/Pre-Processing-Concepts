# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:10:55 2019

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

#Findout the Maximum salary in the column
maximum_salary = dataset['Salary'].max()
print("Maximum Salary:",maximum_salary)
#.....................


#Findout the Minimum salary in the Salary column
minimum_salary = dataset['Salary'].min()
print("Minmum Salary:",minimum_salary)
#.....................


#Findout the Average salary in the Salary column
avg_salary = dataset['Salary'].mean()
print("Average Salary:", avg_salary)
#.....................


#Findout no of values in the Salary column
number_of_values  = dataset['Salary'].count()
print("Average Salary:", number_of_values )
#Finding count of each unique values 
print(dataset['Country'].value_counts())

#.....................


## How to find the unique values in the dataset
#Findout unique values 
print(dataset['Country'].unique())
#Finding count of each unique values 
print(dataset['Country'].value_counts())
#How many null values in the data by eacg column
print(dataset.isnull())
#Finding total null values  by each column
print(dataset.isnull().sum())
#Finding total null values  by whole dataset
print(dataset.isnull().sum().sum())
#.....................


