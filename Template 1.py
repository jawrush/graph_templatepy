# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 00:04:24 2023

@author: Rushiraj Jawale

The following code template is used for plotting X-Y linear graphs from csv or text files.
The data can be collected from experiments and directly used here to plot the graphs.
Lot of customisations options are available for markers, line color, axis limits etc, and everything is well documented using comments.
Please read the comments before using the template. If you are facing problems in using the template,
write to me at jawalerushiraj@gmail.com
"""

#import numpy and matplotlib libraries

import numpy as np
import matplotlib.pyplot as plt


"""
#Read all data present in your files (Here the data is present in txt files) and store it
#It is assumed that the files contain atleast data for 2 variables (X and Y) where X is the independent variable
#You can compare mutiple data of same type by uncommenting the other lines depending on how many data files you want to compare
"""

data1 = np.loadtxt('filename1.txt',skiprows=2) #Use skiprows = no. of rows to skip to skip the rows with text like row headers

"""
data2 = np.loadtxt('filename2.txt',skiprows=2) 
data3 = np.loadtxt('filename3.txt',skiprows=2) 
"""

#Separate the X-values and Y-values from the data loaded in above step

Xval = data1[:,0] #Reads the entire rows of first column
Yval = data1[:,1] #Reads the entire rows of second column

"""
Xval2 = data2[:,0] #Reads the entire rows of first column for data 2
Yval2 = data2[:,1] #Reads the entire rows of second column for data 2
"""

"""
Plot the data and format the plotting (text, markers, marker shape, color, linestyle, linewidth, etc)
Choose from the following and enter in the ax.plot line. Take care of the '' marks in some parameters.

color = cycle[Enter a number from 0 to 9] for different colored lines in the graph or
color = 'enter name of the color' for custom colors. The supported color names can be found on https://matplotlib.org/
label = 'enter name for the line that is plotted'. Used to show what is plotted in then graph and can be used for legend
linewidth = put any number here for the linewidth of the plotted line on the graph. 
marker = 'put marker symbol here'. Supported markers = * (star),p(plus), o(circles), v(triangle), s(square), x(cross), and many more can be found on https://matplotlib.org/
markevery = enter any number. This will change the frequency of the marker points on the plotted data. 
ls = 'choose from - -- or solid, dotted' for changing the linestyle
markersize = enter a number. Controls the size of the markers on the line
"""

plt.rcParams["font.family"] = "Serif"  #Choose font. Serif is good for most research papers
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color'] #Choose default color cycle of matplotlib


#Create axis and sub plot to plot data from multiple files on same graph
 
fig, ax = plt.subplots()  # Create a figure and an axes.

#The actual plotting happens here
ax.plot(Xval,Yval,color=cycle[0], label='label of the graph',linewidth=2.5, marker = 'o', markevery =45, ls='-', markersize = 8 )



ax.set_xlim([xstart, xstop])  #Change the limits of the X-axis for proper representation of your data. Comment the line for automatic limits for X axis
ax.set_xticks([xtick1, xtick2, xtick3, xtickn])  #You can set fixed tick points for X-axis here
ax.set_ylim([ystart, ystop])  #Set the limits for the Y-axis. Comment the codeline for automatic limits for Y-axis
ax.set_yticks([ytick1, ytick2, ytick3, ytickn])  #Set fixed ticks on Y-axis
ax.set_xlabel('X-axis name')  # Add an x-label to the axes.
ax.set_ylabel('Y-axis name')  # Add a y-label to the axes.
ax.minorticks_off() #turn minor ticks off. If you want minor ticks, comment this line

ax.tick_params(which='both', width=1.5)  #Control the width of the ticks on the graph
ax.tick_params(which='major', length=7)  #Control the length of the major ticks
ax.tick_params(which='minor', length=5, color='black')  #Control the length of the minor ticks
ax = fig.gca()
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)
ax.legend(loc = 'upper left')  # Add a legend.
plt.axhline(y= y reference line, color=cycle[5], linewidth = 2, ls='--')  #For plotting any horizontal reference lines. Comment if unused.
plt.axvline(x= x reference line, color=cycle[5],linewidth = 2, ls='--') #For plotting any vertical reference lines. Comment if unused.


#Control the font sizes for various labels and text

plt.rc('axes', titlesize=14)     # fontsize of the axes title
plt.rc('axes', labelsize=14)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
plt.rc('legend', fontsize=14)    # legend fontsize
plt.rc('figure', titlesize=8)  # fontsize of the figure title

#export the graph as pdf or png format. The path by default is the same folder where data and this py file is present.

plt.savefig('grpahname.pdf or .png', format='pdf/png', bbox_inches='tight', transparent=True)
plt.show()  #Display plot inline in your python IDE