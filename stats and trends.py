# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:54:48 2022

@author: USER
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot  as plt

#reading in datasets 
def data_frame_extractor(url, columns_to_delete, rows_to_skip):
  """This function generate data using three args"""
  df = pd.read_excel(url, skiprows=rows_to_skip)
  
    #dropping columns that are not needed. Also, rows with NA were dropped
  df = df.drop(columns_to_delete, axis=1)

    #this extracts a dataframe with countries as column
  df1 = df
    
    #this section extract a dataframe with year as columns
  df2 = df.transpose()

    #removed the original headers after a transpose and dropped the row
    #used as a header
  df2 = df2.rename(columns=df2.iloc[0])
  df2 = df2.drop(index=df2.index[0], axis=0)
  df2 = df2.reset_index()
  df2 = df2.rename(columns={"index":"Year"})
    
  return df1, df2

def create_df_by_country(country, url):
  
    #generate the original data from file/url
df1, df2 = data_frame_extractor(url, columns_to_delete, rows_to_skip)
    
    #create a dataframe
df = pd.DataFrame()
    
    #extract a dataframe of a specific country
for c in country:
        #df = df1[(df1['Country Name'] == c)]
        df = pd.concat([df, df1.loc[df1['Country Name'] == c]])
    
df = df[['Country Name'] + year]
return df