#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt

# generate data: 3 groups and 7 subgroups
group_names=['I. GIS Data',
             'II. Statistical Analysis: \nData Visualization \nPlotting Charts',
             'III. Spatial Analysis'
             ]
group_size=[12,11,30]
subgroup_names=['Data Import', 'Digitizing', 'Export \n.csv Tables',
                'Geological \nPhemomenas', 'Correlation \nAnalysis',
                'Radar Charts', 'Pie Charts', 'Network', 'Bar Charts',
                'Stacked \nBar Charts', 'Andrew Curves'
                ]
subgroup_size=[4,3,5,6,5,5,6,6,6,4,3]

# create colors
a, b, c=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

# 1st ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names,
                  colors=['#7058a3', '#83ccd2', '#ec6d71'])
plt.setp( mypie, width=0.3, edgecolor='white')

# 2nd ring (inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names,
                   labeldistance=0.7,
                   colors=['#a59aca', '#bbbcde', '#bbc8e6',
                           '#c1e4e9', '#a2d7dd', '#f09199', '#ee827c',
                           '#f0908d', '#f2a0a1', '#f5b1aa', '#f6bfbc'
                           ],
                   rotatelabels = 30)
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)

# visualize and save
plt.tight_layout()
plt.savefig('plot_Don.png', dpi=300)
plt.show()
