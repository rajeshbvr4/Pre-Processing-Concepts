# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:24:25 2019

@author: RAJESH
"""

import pandas as pd

df = pd.read_csv("diabetes.csv")

#storing column names into the list type variable
col_names = list(df.columns)


df = df.rename(columns = {col_names[0]:'A',col_names[1]:'B',col_names[2]:'C',col_names[3]:'D',col_names[4]:'E',col_names[5]:'F',col_names[6]:'G',col_names[7]:'H'})

df = df.rename(columns = {1:'I'})


###Dropping coloumns concept 
#Dropping single coloumn from dataset
df = df.drop('A',axis = 1)
#Dropping mutliple coloumns from dataset
df = df.drop(['D','B'],axis = 1)
#Dropping coloumns based on the number 
df = df.drop(df.columns[[0,1]],axis = 1)
#.................



###Dropping rows
df = df.drop(df.index[[3,4,5,5]])
#.....................









