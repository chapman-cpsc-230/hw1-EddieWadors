# -*- coding: utf-8 -*-
"""
File: seconds2years.py 

Copyright (c) 2016 Eddie Wadors

License: MIT

Converting 10 billion seconds into years to determine whether a human could live that long.
"""  
years = float(10**9)/(365.25*24*60*60)
print "the child will easily live to be"   "%.3f years old" % (years)
