#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 23:43:40 2025

Sergio Armenta , Assignment 4 , October 18th, 2025

@author: sergioarmenta
"""

import numpy as np
import matplotlib.pyplot as plt

# Displays the first chart which grabs the data from the file and compares the two datasets
def ComparisonPlot(file1_name, file2_name, x_axis, y_axis):
    # used 'utf-8' so the compiler is able to read all forms of data types
    data1 = np.genfromtxt(file1_name, dtype = None, encoding = 'utf-8') 
    data2 = np.genfromtxt(file2_name, dtype = None, encoding = 'utf-8')
    
    # I used this style of for loop to get some practice with 'for' loops as we did in 87A
    cities = []
    for row in data1:
        cities.append(row[0])
    
    # I also discovered this way of shortening the 'for' loop while using the numpy library
    rainfall1 = np.array([row[1] for row in data1], dtype = float)
    rainfall2 = np.array([row[1] for row in data2], dtype = float)

    x = np.arange(len(cities))
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(x - 0.5/2, rainfall1, width = 0.5, color ='skyblue', label ='Set 1')
    ax.bar(x + 0.5/2, rainfall2, width = 0.5, color ='blue',    label ='Set 2')
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title("Comparison Chart")
    ax.set_xticks(x)
    ax.set_xticklabels(cities, rotation=90)
    ax.legend()
    plt.tight_layout()
    #fig.savefig("RainfallComparisonChart.png", dpi = 300)
    plt.show()
    
    return {"fig" : fig, "ax" : ax, "cities" : cities, "rainfall1" : rainfall1, "rainfall2" : rainfall2}

# uses the compaison chart as an object to produce a seperate chart displaying the comparison chart
# with the Min and Max highlighted 
def MinMax_Comp(chart):
    Rainfall = [chart["rainfall1"], chart["rainfall2"]]
    Set      = ["Set 1", "Set 2"]
    Colors   = ["skyblue", "blue"] 

    for i in range(2): # I did this "for" loop so it runs on both datasets, therefore creating two charts
        Data      = Rainfall[i]
        Set_Name  = Set[i]
        Bar_Color = Colors[i]

        x = np.arange(len(chart["cities"]))
        fig, ax = plt.subplots(figsize = (10,5))
        ax.bar(x, Data, color = Bar_Color, label = Set_Name)

        # I did this to extract and highlight the min and max points
        MinPoint = np.argmin(Data)
        MaxPoint = np.argmax(Data)
        ax.scatter(MinPoint, Data[MinPoint], color = 'red',   s = 100, label = "Min")
        ax.scatter(MaxPoint, Data[MaxPoint], color = 'green', s = 100, label = "Max")

        ax.set_xticks(x)
        ax.set_xticklabels(chart["cities"], rotation = 90)
        ax.set_xlabel("City")
        ax.set_ylabel("Rainfall (in)")
        ax.set_title(f"{Set_Name} - Highlight Min & Max")
        ax.legend()
        plt.tight_layout()
        #fig.savefig(f"RainfallMinMax{Set_Name}Chart.png", dpi = 300)
        plt.show()

# uses the comparison chart again to only display the min and max of both datasets
def MinMax_Only(chart):
    Rainfall   = [chart["rainfall1"], chart["rainfall2"]]
    Set        = ["Set1", "Set2"]
    Color_List = ["skyblue", "blue"]
    Labels     = []
    Values     = []
    Bar_Colors = []  

    for i in range(2):
        Data     = Rainfall[i]
        Set_Name = Set[i]
        Color    = Color_List[i]

        MinPoint = np.argmin(Data)
        MaxPoint = np.argmax(Data)

        Labels.append(f"min - {chart['cities'][MinPoint]} - {Set_Name}")
        Labels.append(f"max - {chart['cities'][MaxPoint]} - {Set_Name}")
        Values.append(Data[MinPoint])
        Values.append(Data[MaxPoint])
        Bar_Colors.extend([Color, Color])  

    x = np.arange(len(Values))
    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x, Values, color = Bar_Colors)
    ax.set_xticks(x)
    ax.set_xticklabels(Labels, rotation = 45)
    ax.set_ylabel("Rainfall")
    ax.set_title("Min/Max Values Only")
    plt.tight_layout()
    #fig.savefig("MinMaxOnlyChart.png", dpi = 300)
    plt.show()

def PieChart(chart):
    Rainfall = chart["rainfall1"]
    Cities   = chart["cities"]
    
    fig, ax = plt.subplots(figsize = (10,10))
    ax.pie(
            Rainfall,
            labels     = Cities, 
            autopct    = '%1.2f%%',   
            startangle = 90,    
            colors     = plt.cm.Set3.colors
    )
    ax.set_title("Rainfall Distribution: Set 1")
    plt.tight_layout()
    #fig.savefig("RainfallSet1PieChart.png", dpi = 300)
    plt.show()

def main():
    RainfallSet1 = "rainfallISet1.txt"
    RainfallSet2 = "rainfallSet2.txt"
    x            = "City"
    y            = "Rainfall (in)"
    Chart1       = ComparisonPlot(RainfallSet1, RainfallSet2, x, y)
    MinMax_Comp(Chart1)
    MinMax_Only(Chart1)
    PieChart(Chart1)
    
main()


"""
Conclusions:
With these visuals, I conclude that rainfall has increased by more than 100% in 
most cities over the span of 10 years, with some cities experiencing more than 
a threefold increase. Bloomfield continues to have the highest levels of rainfall, 
hereas Cascade and Akron’s rainfall levels increased dramatically, making Adine 
the city with the lowest level of precipitation.
"""