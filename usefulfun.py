print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)

    #execrcise
nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)


###
'''filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)'''

###
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

###
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))