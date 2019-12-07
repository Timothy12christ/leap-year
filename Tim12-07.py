# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:01:08 2019

@author: ASUS
"""

s=int(input('What year is it this year?'))
y=s%4
x=s%100 
z=s%400
if y==0 and x!=0:
    print('This year is leap year')
elif z==0:
    print('This year is leap year')
else:
    print('This year is non leap year')