'''Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.'''

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)


evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)



# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)


print("{0}{1}{0}".format("abra", "cad"))


str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)