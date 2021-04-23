#Another type in Python is the Boolean type. There are two Boolean values: True and False.
#They can be created by comparing values, for instance by using the equal operator ==.

my_boolean = True
print(my_boolean)

print(2 == 3)

print("hello" == "hello")

#Be careful not to confuse assignment (one equals sign) with comparison (two equals signs).

#Another comparison operator, the not equal operator (!=),
# evaluates to True if the items being compared aren't equal, and False if they are.
#Comparison operators are also called Relational operators.
print(1 != 1)

print("eleven" != "seven")

print(2 != 10)
#Python also has operators that determine whether one number (float or integer)
# is greater than or smaller than another. These operators are > and < respectively.
print(7 > 5)

print(10 < 10)

print(7 <= 8)

print(9 >= 9.0)#The greater than or equal to, and smaller than or equal to operators are >= and <=.
#They are the same as the strict greater than and smaller than operators,
# except that they return True when comparing equal numbers.

#The first two characters from "Annie" and "Andy" (A and A) are compared. As they are equal,
# the second two characters are compared. Because they are also equal, the third two characters (n and d) are compared.
# And because n has greater alphabetical order value than d, "Annie" is greater than "Andy".
print("Annie" > "Andy")

