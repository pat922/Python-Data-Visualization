import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('./MasterSetFiller.csv',sep=',')

#filter out rows of users that purchased filler treatment
filler_users = df.loc[df['Group']=='FILLER INJECT',['Name','Group','Date']]
filler_users.head()

#all users that have purchased filler and other treatments
dataset = filler_users['Name']
result1 = dataset[dataset['Name'].isin(list(dataset.values))]
result1.head()

#count total number of other treatment group (except filler) purchased by these users
count = result1.groupby(['Group']).size().head() 
df_count2=count.sort_values(ascending = False)
df_count2
df_count2 = df_count2.reset_index()
df_count2.rename(columns={0:'count'}, inplace=True)
 
#retrieve the first row of each customers
result2 = result1.groupby('Name').first()
## [440 rows × 2 columns]
## So, there is 440 users that purchased filler
result3 = result2.loc[result2['Group'] != 'FILLER INJECT']
## [252 rows × 2 columns]
## In these 440 users, 252 of them first purchased treatment is not filler

#put count index 
count3 = dataset.reset_index()
count3.rename(columns={0:'count'}, inplace=True)
df_count3 = count3.sort_values('count', axis = 0, ascending = False, 
                 inplace = True, na_position ='first') 
count3.head()

#merge customers that purchased filler and the treatment they first bought
result4 = pd.merge(result3, filler_xFTP[['Name','Group','Date']],on='Name')

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] ## to remove unnamed cols
export_csv = df.to_csv(r'/usr/local/bin/FTPnotfillerLatest.csv') ## to export csv file 


