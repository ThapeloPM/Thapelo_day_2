# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:33:20 2024

@author: Thapelo
"""

import pandas
file = pandas.read_csv("country_data.csv")

print(file)


file = pandas.read_csv("diab_data.csv")

print(file)

file = pandas.read_csv("housing_data.csv")

print(file)

print(file.info())

file = pandas.read_csv("iris.csv")

print(file)

print(file.info())

file = pandas.read_csv("insurance_data.csv",skiprows=(5))

print(file)
"""
 X      Y
0   108  392.5
1    19   46.2
2    13   15.7
3   124  422.2
4    40  119.4
..  ...    ...
58    9   87.4
59   31  209.8
60   14   95.5
61   53  244.6
62   26  187.5
"""
file = pandas.read_csv("housing_data.csv")

print(file)

column_names = ["A","B", "C", "D", "E", "F", "G", "H", "I"]

file = pandas.read_csv("housing_data.csv", names = column_names)

print(file)