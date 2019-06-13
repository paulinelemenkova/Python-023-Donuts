#!/usr/bin/env python
# coding: utf-8
#
import matplotlib.pyplot as plt
#
# Make data: I have 3 groups and 7 subgroups
group_names=['I. GIS Data', 'III. Spatial Analysis', 'II. Statistical Analysis: \nData Visualization \nPlotting Charts']
group_size=[12,11,30]
subgroup_names=['Data Import', 'Digitizing', 'Export \n.csv Tables', 
                'Geological \nPhemomenas', 'Correlation \nAnalysis', 
                'Radar Charts', 'Pie Charts', 'Network \nFlowchart',
                'Bar Charts', 'Stacked \nBar Charts',
                'Kernel \nDensity \nEstimation']
subgroup_size=[4,3,5,6,5,5,6,5,4,4,6]
#
# Create colors
a, b, c=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
#
# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names,
                  colors=['#7058a3', '#83ccd2', '#ec6d71'] )
plt.setp( mypie, width=0.3, edgecolor='white')
#
# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names,
                   labeldistance=0.7, rotatelabels = 30,
                   colors=['#a59aca', '#bbbcde','#bbc8e6', '#c1e4e9', '#a2d7dd', '#f09199', '#ee827c','#f0908d', '#f2a0a1', '#f5b1aa', '#f6bfbc'])
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)
plt.show()
