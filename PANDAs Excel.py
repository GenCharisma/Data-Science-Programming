# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:31:47 2021

@author: User
"""

import pandas as pd

# Quiz 1
df = pd.read_csv("Salaries.csv")

# first 10 
df.head(10)
# first 20 
df.head(20)
# first 50
df.head(50)
# last few records
df.tail()

# Quiz 2

# 1 Group data using rank
df_rank = df.groupby(['rank'])

# 2 Calculate mean value for each numeric column per each group
df_rank.mean()

# 3 Calculate mean salary for each professor rank
df.groupby('rank')[['salary']].mean()

# 4 Calculate mean salary for each professor rank
df.groupby(['rank'], sort=False)[['salary']].mean()

# 5 Calculate mean salary for each professor rank
df_sub = df[df['salary'] > 120000]

# 6 Select only those rows that contain female professors
df_f = df[df['sex'] == 'Female']

# 7 Select column salary
df['salary']

# 8 Select column salary
df[['rank', 'salary']]

# 9 Select rows by their position
df[10:20]

# 10 Select rows by their labels
df_sub.loc[10:20, ['rank', 'sex', 'salary']]

# 11 Select rows by their labels
df_sub.iloc[10:20, [0, 3, 4, 5]]

# 12 Create a new data frame from the original sorted by the column Salary
df_sorted = df.sort_values(by='service')
df_sorted.head()

# 13
df_sorted = df.sort_values(by = ['service', 'salary'], ascending = [True, False])
df_sorted.head(10)
