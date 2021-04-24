#The words in front of the parentheses are function names,
# and the comma-separated values inside the parentheses are function arguments.

print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3)

#exercise
#The code block within every function starts with a colon (:) and is indented.
def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()

#You must define functions before they are called, in the same way that you must assign variables before using them.

def print_with_exclamation(word):
    print(word + "!")


print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

#2Arguments
'''def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

#exercise
def function(variable):
    variable += 1
    print(variable)

function(7)
print(variable)'''

#exercise
#The return statement cannot be used outside of a function definition.
def max(x, y):
    if x >= y:
        return x
    else:
        return y


print(max(4, 7))
z = max(8, 5)
print(z)

#Exercise

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))

#exercise

def print_numbers():
  print(1)
  print(2)
  return
  print(4)
  print(6)


