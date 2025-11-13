#Partner 1: Ariho Agaba
# Partner 2: Colton Allen
#https://github.com/arihoagaba/Lab11-AA-CA.git
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a): 
    math.sqrt(a)# raise ValueError if a < 0
    
def hypotenuse(a, b): 
    math.hypot(a, b) # can have negative nums

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise ValueError

def exp(a, b):
    return a**b
