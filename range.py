#The range() function returns a sequence of numbers.
#By default, it starts from 0, increments by 1 and stops before the specified number.

numbers = list(range(10))
print(numbers)

#Exercise
nums = list(range(5))
print(nums[4])

#Remember, the second argument is not included in the range, so range(3, 8) will not include the number 8.
numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

#exercise
nums = list(range(5, 8))
print(len(nums))

#range can have a third argument, which determines the interval of the sequence produced, also called the step.
#range(start,stop,step)
numbers = list(range(5, 20, 2))
print(numbers)

#We can also create list of decreasing numbers,
# using a negative number as the third argument, for example list(range(20, 5, -2)).
numb=list(range(20,5,-2))
print(numb)

# Exercise
nums = list(range(3, 15, 3))
print(nums[2])

#exercise
for i in range(5):
    print("hello!")


#exercise
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

#exercise
for i in range(10):
  if not i % 2 == 0:
    print(i+1)

'''FizzBuzz is a well known programming assignment, asked during interviews.

The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn".

You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.'''

n = int(input())

for x in range(1, n):
    if(x%2==0):
        continue
    else:

        if x % 3 == 0 and x % 5 == 0:
            print("SoloLearn")
        elif x % 3 == 0:
            print("Solo")
        elif x % 5 == 0:
            print("Learn")
        else:
            print(x)