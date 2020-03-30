#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:03:19 2020

@author: katerinaroza
"""
#include
import pandas as pd

df = pd.read_csv('twitter_Fear.csv', header=None,error_bad_lines=False)
df.rename(columns={ 1: 'Created_at',2:'Tweet id',4:'Text'}, inplace=True)
df.to_csv('twitter_Fear.csv', index=False) # save to new 
df=pd.read_csv('twitter_Fear.csv',)
x=['Created_at','Tweet id','Text']
newdf=df[x]
newdf.to_csv('twitter_Fear.csv',index=False)