#https://github.com/arihoagaba/Lab11-AA-CA.git
#Partner 1: Ariho Agaba
# Partner 2: Colton Allen
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a): 
    try:
        return math.sqrt(a)
    except:
        raise ValueError
    # raise ValueError if a < 0
    
def hypotenuse(a, b): 
    return math.hypot(a, b) # can have negative nums

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError

def logarithm(a, b):
    return math.log(b, a)

def exp(a, b):
    return a**b
