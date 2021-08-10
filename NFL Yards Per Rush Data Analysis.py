#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import necessary libraries and load dataset into dataframe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

allPlays = pd.read_csv('pbp-2020.csv')


# In[70]:


# create new dataframe of all rushing plays
rushingPlays = allPlays[allPlays['IsRush'] == 1]

# create dataframes for rows with rushes from specified rushing directions
centerRushes = rushingPlays[rushingPlays['RushDirection'] == 'CENTER']
leftGuardRushes = rushingPlays[rushingPlays['RushDirection'] == 'LEFT GUARD']
rightGuardRushes = rushingPlays[rushingPlays['RushDirection'] == 'RIGHT GUARD']
leftTackleRushes = rushingPlays[rushingPlays['RushDirection'] == 'LEFT TACKLE']
rightTackleRushes = rushingPlays[rushingPlays['RushDirection'] == 'RIGHT TACKLE']
leftEndRushes = rushingPlays[rushingPlays['RushDirection'] == 'LEFT END']
rightEndRushes = rushingPlays[rushingPlays['RushDirection'] == 'RIGHT END']

# calculate yards per rush for each rushing direction
centerYPR = centerRushes['Yards'].sum() / centerRushes.shape[0]
leftGuardYPR = leftGuardRushes['Yards'].sum() / leftGuardRushes.shape[0]
rightGuardYPR = rightGuardRushes['Yards'].sum() / rightGuardRushes.shape[0]
leftTackleYPR = leftTackleRushes['Yards'].sum() / leftTackleRushes.shape[0]
rightTackleYPR = rightTackleRushes['Yards'].sum() / rightTackleRushes.shape[0]
leftEndYPR = leftEndRushes['Yards'].sum() / leftEndRushes.shape[0]
rightEndYPR = rightEndRushes['Yards'].sum() / rightEndRushes.shape[0]

# list to store yards per rush variables for use in matplotlib portion
rushesYPR = [centerYPR, leftGuardYPR, rightGuardYPR, leftTackleYPR, rightTackleYPR, leftEndYPR, rightEndYPR]


# In[72]:


# specify labels for x/y axis, individual bars, and set amount of values for bar graph
labels = ['Center', 'Left Guard', 'Right Guard', 'Left Tackle', 'Right Tackle', 'Left End', 'Right End']
plt.xticks(range(len(rushesYPR)), labels)
plt.xlabel('Run Direction')
plt.ylabel('Yards Per Rush')
plt.title('2020 NFL Season Yards Per Rushing Direction')

# create bars for graph from values of the rushesYPR list
plt.bar(range(len(rushesYPR)), rushesYPR) 

# display value of each bar within the bar
for index, value in enumerate(rushesYPR):
    plt.text(index-0.30, value-1, str(value.round(3)))
    
# add grid for y values and rotate x-axis labels by 45 degrees
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
plt.xticks(rotation=45)

# display bar graph
plt.show()


# In[ ]:




