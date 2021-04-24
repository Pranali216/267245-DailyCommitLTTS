#functions as objects
def multiply(x, y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))

#The example above assigned the function multiply to a variable operation.
# Now, the name operation can also be used to call the function.

#Functions can also be used as arguments of other functions.
def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))




