# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import math

nfl = pd.read_csv("NFL Play by Play 2009-2017 (v4).csv", nrows = 1)
len(list(nfl.columns)) # 102 columns

nfl = pd.read_csv("NFL Play by Play 2009-2017 (v4).csv")
nfl.head # we can see some NaN values

permits = pd.read_csv("Building_Permits.csv", nrows = 1)
len(list(permits.columns)) # 43
permits = pd.read_csv("Building_Permits.csv")
permits.head


# we can also just use the .shape method to find out the columns, as well as rows
nfl.shape # rows is at index 0, columns at index 1
permits.shape


# find which cells are NULL
nfl.isna() # alias for .isnull(), but most reminiscent of R
permits.isna()

# we can get a count for each column's NA/NULL (NaN values), though
nfl.isna().sum()
permits.isna().sum()

# drop all rows that contain missing value. default axis = 0
nfl.dropna() # no rows left!
permits.dropna() # no rows left!

# instead, remove columns with missing values
nfl_removed_cols = nfl.dropna(axis = 1)
permits_removed_cols = permits.dropna(axis = 1)

nfl.shape[1] - nfl_removed_cols.shape[1] # 61 columns removed
permits.shape[1] - permits_removed_cols.shape[1] #31 removed cols

# return a subset of columns
list(nfl.columns) # return all columns
nfl.columns.get_loc("EPA") # index of column EPA
nfl.columns.get_loc("Season") # index of column Season; index 101, last col
subset_nfl = nfl.loc[:, 'EPA':'Season'].head() # returns columns EPA - Season

# get specific column
nfl.Season
nfl.Season[0] # index of columm
nfl.loc[[1,2,4], ["EPA", "Season"]] # slice 1,2,4 (rows) and only two cols

