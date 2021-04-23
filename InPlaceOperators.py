#In-place operators allow you to write code like 'x = x + 3' more concisely, as 'x += 3'.
#The same thing is possible with other operators such as -, *, / and % as well.

x = 2
print(x)
x += 3
print(x)


x *= 3
print(x)


x = "spam"
print(x)
x += "eggs"
print(x)

#In-place operators can be used for any numerical operation (+, -, *, /, %, **, //).

x="a"

x*=5
print(x)

#&&&&&&&&&&&&&&&
spam="7"
spam=spam +"0"
eggs=int(spam)+3
print(float(eggs))