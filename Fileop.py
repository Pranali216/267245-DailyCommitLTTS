'''You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).'''


# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

'''You can use the + sign with each of the modes above to give them extra access to files. 
For example, r+ opens the file for both reading and writing.'''

'''To read only a certain amount of a file, you can provide a number as an argument to the read function. 
This determines the number of bytes that should be read.
You can make more calls to read on the same file object to read more of the file byte by byte. 
With no argument, read returns the rest of the file.'''

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

'''To retrieve each line in a file,
 you can use the readlines method to return a list in which each element is a line in the file.'''

'''An alternative way of doing this is using with statements. This creates a temporary variable (often called f), 
which is only accessible in the indented block of the with statement.


with open("filename.txt") as f:
   print(f.read())'''

