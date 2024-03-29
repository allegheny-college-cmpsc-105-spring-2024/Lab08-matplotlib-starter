# import statements

import numpy as np
import matplotlib.pyplot as plt

#%% - regular line (only y specified)

plt.subplots()
plt.plot([1, 2, 3, 4])
plt.ylabel('y values')

#%% - regular line with x and y specified

plt.subplots()
plt.plot([1, 2, 3, 4], [1, 16, 9, 4])

# QUESTION: which list is for x?
# QUESTION: which list is for y?

#%% - regular line with x and y specified

plt.subplots()
plt.plot([3, 1, 4, 2])

#%% - formatting

plt.subplots()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

# QUESTION: What happened?

#%%

plt.subplots() # start a new figure
plt.pie([1,4,5], labels = ["l1", "l4", "l5"]) # pie chart
plt.title("Pie Chart")


#%%  generate some randm data for more interesting plotting examples

dataline = np.array([1,2,3,4,5,6,7,8,9])

alpha = 0.05
# Make gaussian data
mu, sigma = 0, 1 # population mean and sd
normdata = np.random.normal(mu, sigma, 1000000)



#%% - more formatting

plt.subplots()
plt.plot(dataline, 'r--')
plt.plot(dataline**2, 'bs')
plt.plot(dataline**3, 'g^')

# QUESTION: What happened?

#%% legends

plt.subplots()
plt.plot(dataline, 'r--')
plt.plot(dataline**2, 'bs')
plt.plot(dataline**3, 'g^')
plt.plot(-1*dataline**3, linewidth=12.0)

plt.legend(('values', 'values**2', 'values**3', '-1 * values**3'))

# QUESTION: What happened?

#%% error bars - usually used for SEM

m_dl = np.mean(dataline)

plt.subplots()
plt.bar([1,2,3], [m_dl, 11, 12])
# change the labels on x axis - tick position, tick label
plt.xticks([1,2,3], ["mean dataline", "test2", "test3"])

# errorbar needs x pos, y pos, yerr which is the error bar around y 
plt.errorbar([1], [m_dl], yerr=[3])
plt.errorbar([2], [11], yerr=[50], ecolor='b' )

# QUESTION: can you add an error bar for the last x,y bar pair

#%%

fig, ax = plt.subplots() # start a new figure
plt.boxplot(normdata) # box plot
plt.xlabel("dataset") # label
plt.ylabel("value") # label
plt.title("Box plot") # title

#%%

plt.subplots() # start a new figure
plt.hist(normdata, bins = 10) # historgram
plt.xlabel("value") # label
plt.ylabel("frequency") # label
plt.title("Historgram") # title


#%%

plt.subplots() # start a new figure
plt.violinplot(normdata) # violin plot
plt.xlabel("dataset") # label
plt.ylabel("frequency") # label
plt.title("Violin Plot") # title

#%%

plt.subplots() # start a new figure
plt.plot(normdata) # line plot
plt.xlabel("order") # label
plt.ylabel("value") # label
plt.xlim((0, 100)) # limit the view
plt.title("Line plot") # title

