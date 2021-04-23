print("Spam" + 'eggs')

print("2" + "2")

#Adding a string to a number produces an error, as even though they might look similar, they are two different entities.

print("String" + "2")
print('1' + "Two")


#Strings can also be multiplied by integers. This produces a repeated version of the original string.
# The order of the string and the integer doesn't matter, but the string usually comes first.

print("spam" * 3)

print(4 * '2')

#VARIABLES
#Certain restrictions apply in regard to the characters that may be used in Python variable names.
# The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
#Python is case sensitive

user = "James"
abc="this is small abc variable"
ABC="This is capital ABC variable"
this_is_a_normal_variable_declaration_with_underscores_alphabets_and_numbers_allowed="Rules of declaration of variable"

print(user)
print(abc)
print(ABC)
print(this_is_a_normal_variable_declaration_with_underscores_alphabets_and_numbers_allowed)

# Operations on variables
x = 7
print(x)

print(x + 3)

print(x)

#One more example
spam="eggs"
print(spam*3)
# spam is a variable with stored value eggs and it is multiplied by 3 .... so eggs three times will be printed.


#Variables can be reassigned as many times as you want, in order to change their value.
#In Python,
#variables don't have specific types, so you can assign a string to a variable, and later assign an integer to the same variable.
x = 123.456
print(x)

x = "This is a string"
print(x + "!")

