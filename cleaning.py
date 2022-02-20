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

# find which cells are NULL
nfl.isna() # alias for .isnull(), but most reminiscent of R
permits.isna()

# we can get a count for each column's NA/NULL (NaN values), though
nfl.isna().sum()
permits.isna().sum()
