#!/usr/bin/env python
# coding: utf-8

# In[100]:


#In this project, I am importing, cleaning, and visualizing data from a meditation app that I have used for three years. 


# In[99]:


import pandas as pd
df=pd.read_csv(r"C:\\Users\alexa\Desktop\app.csv")
print(df[r"Started At"])

#The Started At column contains the day and time of when I started my meditation session. I would like to change it to separate out the date and time.

df['day'], df['time'] =df[r"Started At"].str.split(' ', 1).str
print(df['day'])
print(df['time'])

df.rename(columns={'Started At': 'Started At', 'day': 'date', 'time':'time'}, inplace=True)
df.head()
df['hour'], df['minute']=df['time'].str.split(':', 1).str
df.print()


# In[103]:


#Splitting Up the Duration into Hrs, Minutes, and Seconds
df['hrs_meditated'], df['minutes_meditated'], df['seconds_meditated']=df['Duration'].str.split(':', 2).str
df.head()
#Converting to Integers in order to perform calculations
df['hrs_med_int']=df['hrs_meditated'].astype(int)
df['min_med_int']=df['minutes_meditated'].astype(int)
df['sec_med_int']=df['seconds_meditated'].astype(int)
df['tot_minutes']=(df['hrs_med_int']*60)+df['min_med_int']+df['sec_med_int']/60
df['hour_of_day']=df['hour'].astype(int)
print(df)


# In[98]:


import matplotlib.pyplot as plt
import numpy as np
#Creating a bar chart to see when I meditate the most. Looks like the morning!
plt.bar(df['hour_of_day'], df['tot_minutes'])
plt.xlabel('Hour of Day')
plt.ylabel('Total Minutes Meditated')
plt.title('When do I meditate?')


# In[105]:


#Extracting the year from the date column.
df['date_month'], df['date_day'], df['date_year']=df['date'].str.split('/', 2).str

df['date_year_int']=df['date_year'].astype(int)
plt.bar(df['date_year_int'], df['tot_minutes'])
plt.xlabel('Year')
plt.ylabel('Total Minutes Meditated')
plt.title('How Much Do I Meditate Each Year?')


# In[ ]:





# In[ ]:




