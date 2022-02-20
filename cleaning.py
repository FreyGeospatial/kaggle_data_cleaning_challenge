# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
nfl = pd.read_csv("NFL Play by Play 2009-2017 (v4).csv", nrows = 1)
len(list(nfl.columns)) # 102 columns

# read in all columns as strings to prevent pandas from guessing the wrong data types
nfl = pd.read_csv("NFL Play by Play 2009-2017 (v4).csv", dtype = str)
nfl.head

permits = pd.read_csv("Building_Permits.csv", nrows = 1)
len(list(permits.columns)) # 43
permits = pd.read_csv("Building_Permits.csv", dtype = str)
permits.head

