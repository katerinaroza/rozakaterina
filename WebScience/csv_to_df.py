#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:38:46 2020

@author: katerinaroza
"""

import pandas as pd
file_name = "twitter_Fear.csv"
file_name_output = "twitter_Fear2.csv"

df = pd.read_csv(file_name, sep="\t or ,",engine='python')

# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  
df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
df.to_csv(file_name_output)