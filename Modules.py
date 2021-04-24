'''Modules are pieces of code that other people have written to fulfill common tasks, such as generating random numbers, performing mathematical operations, etc.

The basic way to use a module is to add import module_name at the top of your code,
and then using module_name.var to access functions and values with the name var in the module.
For example, the following example uses the random module to generate random numbers:'''

import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)
#the above program will print any random 5 numbers  in between 1 to 6


'''There is another kind of import that can be used if you only need certain functions from a module.
These take the form from module_name import var, and then var can be used as if it were defined normally in your code.
For example, to import only the pi constant from the math module:'''

from math import pi

print(pi)

'''* imports all objects from a module. For example: from math import *
This is generally discouraged, as it confuses variables in your code with variables in the external module.'''

#trying to import a module that isn't available causes an ImportError.

'''You can import a module or object under a different name using the as keyword. 
This is mainly used when a module or object has a long or confusing name.'''
from math import sqrt as square_root
print(square_root(100))

#pip=Python Package Index

def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)

#exercise
def func(x):
  res = 0
  for i in range(x):  #0-3 //0//1//2//3
     res =res + i #//0//1//3//6
  return res

print(func(4))


#exercise
celsius = int(input())


def conv(c):
    return 9 / 5 * celsius + 32


fahrenheit = conv(celsius)
print(fahrenheit)