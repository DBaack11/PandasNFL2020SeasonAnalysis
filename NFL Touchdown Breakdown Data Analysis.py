#!/usr/bin/env python
# coding: utf-8

# In[248]:


# import necessary libraries and load dataset into dataframe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

allPlays = pd.read_csv('pbp-2020.csv')


# In[249]:


# load all plays resulting in a touchdown into a new dataframe
touchdowns = allPlays[allPlays['IsTouchdown'] == 1]

# separate touchdowns in each quarter in separate dataframes
firstQTDS = touchdowns[touchdowns['Quarter'] == 1]
secondQTDS = touchdowns[touchdowns['Quarter'] == 2]
thirdQTDS = touchdowns[touchdowns['Quarter'] == 3]
fourthQTDS = touchdowns[touchdowns['Quarter'] == 4]
fifthQTDS = touchdowns[touchdowns['Quarter'] == 5]

# 2D array for touchdowns in each quarter broken down by what down they were scored on
TDDowns = [[],[],[],[],[]]

# loop to retrieve touchdowns scored on each down within each quarter and stored in 2D array
for i in range(0,4):
    quarter1 = firstQTDS[firstQTDS['Down'] == i+1].shape[0]
    quarter2 = secondQTDS[secondQTDS['Down'] == i+1].shape[0]
    quarter3 = thirdQTDS[thirdQTDS['Down'] == i+1].shape[0]
    quarter4 = fourthQTDS[fourthQTDS['Down'] == i+1].shape[0]
    quarter5 = fifthQTDS[fifthQTDS['Down'] == i+1].shape[0]
    
    TDDowns[0].append(quarter1)
    TDDowns[1].append(quarter2)
    TDDowns[2].append(quarter3)
    TDDowns[3].append(quarter4)
    TDDowns[4].append(quarter5)


# In[250]:


# create new dataframe of 2D array TDDowns with labels for each quarter
plotdata = pd.DataFrame(data = TDDowns, index=['First\nQuarter', 'Second\nQuarter', 'Third\nQuarter', 'Fourth\nQuarter','Overtime'])

# create stacked bar chart from new dataframe and add labels to the matplotlib plot
plotdata.plot(kind="bar", stacked=True)
plt.title("2020 NFL Season Touchdown Breakdown (By Quarter and Downs)")
plt.ylabel("Total Touchdowns Scored")
plt.legend(['1st Down', '2nd Down', '3rd Down', '4th Down'], loc='upper right', bbox_to_anchor=(1.18,1), prop={'size':13})

# add grid lines to the chart, specify increment amount for y axis, and rotate labels on x axis
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
plt.yticks(np.arange(0,600, 50))
plt.xticks(rotation=0)
  
# add touchdown total labels for each quarter
for i in range(0,5):
    total = sum(TDDowns[i])
    plt.text(i-0.13,i+total+5, total)
    
# add table with touchdown down totals for each quarter below bar chart
plt.table(cellText=np.transpose(TDDowns),
          rowLabels=['1st Down', '2nd Down', '3rd Down', '4th Down'],
          rowColours=['#1f77b4','#ff7f0e','#2ca02c','#d62728'],
          loc='bottom', bbox=[0.0,-0.55,1.0,0.4],
          cellLoc='center')
# show matplotlib plot
plt.show()


# In[ ]:





# In[ ]:




