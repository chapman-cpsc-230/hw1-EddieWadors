# -*- coding: utf-8 -*-
"""
File: Interest_rate.py

Copyright (c) 2016 Eddie Wadors

License: MIT

Converting an interest rate over years formula into python.
"""
A=1000
P=.05
years = 3
sum = float (A * (1 + P/100)**years)
print sum
