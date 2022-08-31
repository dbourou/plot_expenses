#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:40:07 2021

@author: usuari
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#must be in a form where variables are separate columns
df = pd.read_excel("bank_movement.xlsx")

#IMPORT THE EXCEL FILE OF YOUR BANK MOVEMENTS HERE

#df = pd.read_excel("expenses_last_year.xlsx")


#vars of type Dataframe


'''
Let's plot some data.

Variable names in order:
'Operation date', 'Item', 'Value date', 'Amount', 'Balance',
'reference 1', 'Reference 2'
'''

#data = df[['Operation date','Item','Amount']]

date     = list(df['Operation date'])
item     = list(df['Item'])
cost     = list(df['Amount'])
item_cat = ['Misc'] * len(item)
balance= list(df['Balance'])


# NEWEST ARE FIRST!!!

#HERE YOU CAN OPTIONALLY SELECT A SPECIFIC PERIOD TO PLOT
#YOUR ACCOUNT BALANCE AND THE TYPE OF EXPENSES YOU MADE

'''
date = date[150:]
item = item[150:]
cost = cost[150:]
item_cat= item_cat[150:]
balance= balance[150:]
'''


plt.plot(date,balance)
plt.show()


'''
plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(country,BoT,marker='*',s=100,edgecolors='black',c='yellow')
plt.title('Countries BoT')
plt.show()

#calculate BoT as percentage of GDP perhaps?

'''

#put text from how the expenses appear in the excel file
#you can add as many as you want but must also add the corresponding
#category you want it to be, in the ''codes'' list

labels = ['gym_name', #--> gym #PUT GYM NAME HERE
          'supermarket_1', 'supermarket_2' #--> groceries
          #PUT SUPERMARKET NAMES HERE
          'amazon', 'amzn', #--> Amazon
          'artbo', # --> Dessert
          'ametller', # --> deli groceries
          'restaurant_1' #--> restaurants
          #PUT RESTAURANT NAMES HERE
          'FF.CC. generalitat', 'metro', 'renfe', 'tmb', #--> transportation
          'vodafone', 'cosmote', #--> phone bills
          'landlords_name', #--> rent #PUT YOUR LANDLORDS NAME
          'fisioterapeuta']

labels2 = [x.upper() for x in labels]


codes = ['Gym',
         'Groceries','Groceries',
         'Amazon','Amazon',
         'Deli groceries',
         'Deli groceries',
         'Restaurants',
         'Transportation','Transportation','Transportation','Transportation',
         'Phone bills','Phone bills',
         'Rent',
         'Physiotherapy']


codes2 = [x.upper() for x in codes]

for i in range(0,len(item)):
    for c in labels2:
        if c in item[i]:
            item_cat[i] = codes[labels2.index(c)]
        else: continue
    

#seems to get in both loops normally, idk whats the issue


classes = set()
for x in codes:
    classes.add(x)
    
classes=sorted(list(classes),key=str.lower)


#classes.append('Misc')

class_amount = []

colors = ['None'] * len(item_cat)
color_list = ['lightgrey','paleturquoise','pink','peachpuff','palegreen',
              'lightskyblue','thistle','limegreen','wheat']

#classes.append('Misc')

for s in classes:
    current_color = color_list[classes.index(s)]
    sum = 0
    for l in item_cat:
        if s in l:
            sum = sum + cost[item_cat.index(l)]
            colors[item_cat.index(l)] = current_color #this fails
            #colors.append(current_color)
        else: continue
    
    class_amount.append(abs(sum))





def autopct_generator(limit):
    """Remove percent on small slices."""
    def inner_autopct(pct):
        return ('%.2f%%' % pct) if pct > limit else ''
    return inner_autopct



labels = classes
sizes = class_amount

fig1, ax1 = plt.subplots(figsize=(6, 5))


box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 1.3, box.height])

total = 0
for i in class_amount:
    total += i


_, _, autotexts = ax1.pie(
    sizes, colors=color_list, autopct=autopct_generator(7), startangle=90, radius=1.8 * 1000, frame=True)
for autotext in autotexts:
    autotext.set_weight('bold')
ax1.axis('equal')
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (s / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 12},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure
)
# fig1.set_size_inches(18.5, 10.5)
fig1.savefig('chart.png')







