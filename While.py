#The code in the body of a while loop is executed repeatedly. This is called iteration.
i = 1
while i <=5:
    print(i)
    i = i + 1

print("Finished!")

#exercise
i = 3
while i>=0:
   print(i)
   i = i - 1

#exercise
x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1
#To end a while loop prematurely, the break statement can be used.
#For example, we can break an infinite loop if some condition is met:

i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

#exercise
i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break


#Another statement that can be used within loops is continue.
#Unlike break, continue jumps back to the top of the loop, rather than stopping it. Basically,
#the continue statement stops the current iteration and continues with the next one.

i = 0
while True:
    i = i +1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished")