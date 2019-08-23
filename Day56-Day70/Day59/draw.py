
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.pyplot import Line2D

def draw_level(each_level):
    ylim=ax1.get_ylim()[1]
    xlim=ax1.get_xlim()[1]
    each_level=np.array(each_level)
    each_col=xlim/((len(each_level)))
    each_row=ylim/np.amax(each_level)
    radius=0.4*each_row
    for i,item in enumerate(each_level):
        # your code here

def draw_line(each_level):
    ylim = ax1.get_ylim()[1]
    xlim = ax1.get_xlim()[1]
    each_level = np.array(each_level)
    each_col = xlim / ((len(each_level)) )
    each_row = ylim / np.amax(each_level)
    result=list()
    for i, item in enumerate(each_level):
        # your code here
    for i in range(len(each_level)-1):
        for item in result[i]:
            for i_next in result[i+1]:
                # your code here 

fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.set_xlim(0,10)
ax1.set_ylim(0,10)
ax1.set_aspect(1)
each_level=[3,5,9,6]
draw_line(each_level)
draw_level(each_level)
plt.show()
