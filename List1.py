#Lists are used to store items.
#A list is created using square brackets with commas separating items.

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

#empty list

empty_list = []
print(empty_list)

#In some code samples you might see a comma after the last item in the list.
# It's not mandatory, but perfectly valid.

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

#Matrix list
m = [
    [1, 2, 3],
    [4, 5, 6]
]

print(m[1][2])

#String
#Some types, such as strings, can be indexed like lists.
#Indexing strings behaves as though you are indexing a list containing each character in the string.
#Space (" ") is also a symbol and has an index.
str = "Hello world!"
print(str[6])


#The item at a certain index in a list can be reassigned.
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

#Lists can be added and multiplied in the same way as strings.
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

#To check if an item is in a list, the in operator can be used.
#It returns True if the item occurs one or more times in the list, and False if it doesn't.

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#exercise
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])

#To check if an item is not in a list, you can use the not operator in one of the following ways:
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#exercise
letters=['a','b','z']
if 'z' in letters:
    print("yes,z is in the list")
else:
    print("Z is not list")

#APPEND FUNCTION
#The append method adds an item to the end of an existing list.

nums = [1, 2, 3]
nums.append(4)
print(nums)

words = ["hello"]
words.append("world")
print(words[1])

#To get the number of items in a list, you can use the len function.
#Unlike the index of the items, len does not start with 0. So, the list above contains 5 items, meaning len will return 5.
#len is written before the list it is being called on, without a dot.

nums = [1, 3, 5, 2, 4]
print(len(nums))

#The insert method is similar to append, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

#The index method finds the first occurrence of a list item and returns its index.
#If the item isn't in the list, it raises a ValueError.
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))   #item is not in the list so error is raised

'''max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(item): Returns a count of how many times an item occurs in a list
list.remove(item): Removes an object from a list
list.reverse(): Reverses items in a list.
for example, you can count how many 42s are there in the list using:
items.count(42)
where items is the name of our list.'''



