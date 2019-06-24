#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 00:55:36 2019

@author: skwatra@us.ibm.com
"""


import pandas as pd
from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [1, 4, 5]
z = [6, 4, 1]
plt.plot(x,y)
plt.plot(x,z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y")
plt.ylabel("z")
plt.legend(["this is y", "this is z"])
plt.show()
print("\n")

sample_data = pd.read_csv('sample_data.csv')

print(sample_data)
print("\n")
print(type(sample_data))
print("\n")
print(sample_data.column_c) 
print("\n")
plt.plot(sample_data.column_a, sample_data.column_b)
plt.plot(sample_data.column_a, sample_data.column_c)
plt.xlabel('column a')
plt.ylabel('column b/c')
plt.legend(['column b','column c' ])
plt.show()
print("\n")
df = pd.read_csv('countries.csv')

print(df.head())
print("\n")
#compare the population of us and india
us = df[df.country == 'United States']
print(us)
us.population.iloc[0]
print("\n")
print(us.population/us.population.iloc[0] * 100)

india= df[df.country =='India']
print("\n")
print(india)

china = df[df.country=='China']
print("\n")
print(china)

print("\nLets plot the years vs population for India, US and China")
plt.plot(india.year, india.population/10**6)
plt.plot(us.year,us.population/10**6)
plt.plot(china.year,china.population/10**6)
plt.legend(['India', 'United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()


print("Lets see the % difference in population in US and China")
plt.plot(us.year,us.population/us.population.iloc[0] * 100)
plt.plot(us.year, china.population/china.population.iloc[0]*100)
plt.xlabel('year')
plt.ylabel('population')
plt.show() 