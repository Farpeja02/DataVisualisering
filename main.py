import csv
import numpy as np
from matplotlib import pyplot as plt

completeList = [] #The complete list 2d lists are created with.
with open('temperature.csv', newline='') as csvfile: #Opens the CSV file
    spamreader = csv.DictReader(csvfile, delimiter=',') #With the opened file this creates a dict with every row being a dict. The delimiter is set to: ,

    for row in spamreader: #Looks through every row in the spamreader.
        if 'SWE' in row['country_id']: #Only continues if the country_id is SWE for Sweden.
            if 'NA' in row['AverageTemperatureFahr']:#Checks if the AverageTemperatureFahr is empty
                continue #Continue jumps over the rest of the going round if the AverageTemperatureFahr is empty
            if  '06' in row['month']: #Only records data in june
                if '01' in row['day']:#Only records data for the 1st
                    tempList = [] #Creates a temp list.
                    tempList.append(row['year']) #Puts the year into the temp list
                    tempList.append((float(row['AverageTemperatureFahr']) - 32) / 1.8)#Converts the data to celsius and puts it into the temp list
                    completeList.append(tempList)#Adds the temp list to the complete list creating 2d lists.
sortedCompleteList = sorted(completeList, key=lambda x: x[0]) #Sorts the 2d lists by year by looking at the first value in each inner list.

x = [] #Creates 2 empty lists for the plotting
y = []

for D,T in sortedCompleteList: #Takes the 2d list and puts all the years in the list named X, and all the tempatures in the list named Y.
    x.append(D)
    y.append(T)

X = np.array(x) #Puts the data into a np array.
Y = np.array(y)
plt.title("The temperature in Sweden on the first of June from 1744 -> 2013") #Title for the plot
plt.xlabel("Year") #Title for the X axis
plt.ylabel("Temperature in celsius") #Title for the Y axis
plt.plot(X,Y) #Plots the data
plt.show() #Creates the png of the plot
