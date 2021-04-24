#In the code above, the word variable represents the corresponding item of the list in each iteration of the loop.
#During the 1st iteration, word is equal to "hello", and during the 2nd iteration it's equal to "world", and so on.

words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

#exercise
str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)

#exercise
list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break


'''for vs while


Both, for and while loops can be used to execute a block of code for multiple times.

It is common to use the for loop when the number of iterations is fixed. For example, 
iterating over a fixed list of items in a shopping list.

The while loop is used in cases when the number of iterations is not known and depends on some 
calculations and conditions in the code block of the loop.
For example, ending the loop when the user enters a specific input in a calculator program.
Both, for and while loops can be used to achieve the same results, however, the for loop has cleaner and shorter syntax
, making it a better choice in most cases.
'''
