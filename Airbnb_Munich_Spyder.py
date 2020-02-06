# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:24:36 2020

@author: Ashwin
"""
import pandas as pd



listings = pd.read_csv('listings.csv')
calendar = pd.read_csv('calendar.csv')
reviews = pd.read_csv('reviews.csv')

listings.head()

"$" in listings['security_deposit'].str.cat(sep=' ')
"$" in listings['id'].astype(str).str.cat(sep=' ')


listings['id'].astype(str)
