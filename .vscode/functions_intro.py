import math
"""
functions are either void or fruitful
"""
#Global Variability
f_name = ""

#FUNCTION DEFINITIONS
#void function
def setName(name):
    #fname is the local variable
    #f_name is the global variable
    f_name.set(fname)
    print(f_name)

#fruitful function
def getName():
    return f_name

def sum(numbers):
    sum = 0 
    for i in numbers: #
        sum += i  #. += sum = sum + i
    return sum
print(sum)

#function calls
"""
function <- adds all the numeric values within a list
author: Poly (10-8-25)
"""

num1 = (1,2,3,4,5,6,7,8,9,10)
num2 = (2,3,4,5,6,7,8,9,10)
num3 = (2.3,3.4,4.5,5.6,6.7)
test1 = sum(num1)
print(test1)
sum(num1)

def absValue(x):
    if x < 0:
        return -x #the return statement exits the function 
    return x

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    

def distance(x1, y1, x2, y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
print(distance(1,2,3,4))


# boolean functions return a true or false 
# examples of boolan functions are:
# -is age 16
# -is the pwd correct

#Fun Fact: boolean functions are normally name is ___
def isDivisable(x, y):
    if (x % y == 0):
        return True
    return False
print(isDivisable(10, 2))
print(isDivisable(3, 2))
print(isDivisable(12, 6))