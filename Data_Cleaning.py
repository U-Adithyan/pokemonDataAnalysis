"""
Created on Sat May 14 19:54:32 2022
@author: U Adithyan
"""
import pandas as pd
import numpy as np

df=pd.read_csv("./Pokemon.csv")

#fill nan in type2
df['Type 2'].fillna('N/A', inplace=True)

#fix special names
df['Name'] = df['Name'].str.replace(".*(?=Mega)", "")
df['Name'] = df['Name'].str.replace(".*(?=Primal)", "")
df['Name'] = df['Name'].str.replace(".*(?=Hoopa)", "")

#changing Legendary Column to Integer Values
df['Legendary']=df['Legendary'].apply(lambda x: 1 if x==True else 0)

#add mega as a column
df['Mega']=df['Name'].apply(lambda x: 1 if 'mega ' in x.lower() else 0)

#fix mega generation
df.loc[df['Mega']==True,'Generation']=6

df.to_csv("Pokemon_Data_Cleaned.csv",index=False)