print(1 == 1 and 2 == 2)

print(1 == 1 and 2 == 3)

print(1 != 1 and 2 == 2)

print(2 < 1 and 3 >  6)

#********************************************************

if (1 == 1) and (2 + 2 > 3):
  print("true")
else:
  print("false")

#********************************************************

print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3 >  6)

#*********************************************************

print(not 1 == 1)

print(not 1 > 7)

#************************************************************

if not True:
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")

#********************************************************

#The below code shows that == has a higher precedence than or
#Python's order of operations is the same as that of normal mathematics:
# parentheses first, then exponentiation, then multiplication/division, and then addition/subtraction.

print(False == False or True)

print(False == (False or True))

print((False == False) or True)

#**************************************************

if 1 + 1 * 3 == 6:
   print("Yes")
else:
   print("No")

#***************************************************

grade = 88
if(grade >= 70 and grade <= 100):
    print("Passed!")

#****************************************************
    x = 4
    y = 2
    if not 1 + 1 == y or x == 4 and 7 == 8:
        print("Yes")
    elif x > y:
        print("No")



