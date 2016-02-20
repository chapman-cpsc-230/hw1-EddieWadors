# -*- coding: utf-8 -*-
"""
File: sin2_plus_cos2.py

Copyright (c) 2016 Eddie Wadors

License: MIT

Finding Bugs in python code given by the textbook
"""
print "Fixed Code A"
from math import sin, cos, pi
x = pi/4
val = sin(x)**2 + cos(x)**2
print val

print "Fixed Code B"
v0 = 3
t = 1
a = 2/t**2
s = v0*t + 0.5*a*t**2
print s

print "Fixed Code C" 
a = 3.3
b = 5.3
a2 = (a**2)
b2 = (b**2)

eq_sum1 = a2 + 2.0*(a*b) + b2
eq_sum2 = a2 - 2.0*(a*b) + b2

eq_pow1 = (a + b)**2
eq_pow2 = (a - b)**2

print 'First Equation: %g = %g' % (eq_sum1, eq_pow1)
print 'Second Equation: %d = %d' % (eq_pow1, eq_pow2)
