# -*- coding: utf-8 -*-
"""
Created on Sun May  6 20:29:09 2018

@author: lc
"""

# =============================================================================
# Fibonacci
# =============================================================================
def fib(x):
    if x<=2:
        return x
    else:
        return fib(x-1)+fib(x-2)

def sq(x):
    return x**2
    
list(map(fib,range(7)))


