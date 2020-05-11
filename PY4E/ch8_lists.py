# List is a collection
friends = ['Joseph', 'Glenn', 'Sally']
print(friends)
print(type(friends))

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)

# List can contains any object that is present in python. int or float or list, strings
student = ['Ahmad', 19, 65.4, [78, 80, 85]]
print(student)
print(len(student))

# List Constants
print(2)
print([1, 2, 3])
print(['red', 'yellow', 'blue'])

# Looking inside a list
dress = ['socks', 'shirt', 'perfume']
print(dress[1])

# list index out of range
print(dress[3])

# If an index has a negative value, it counts backward from the end of the list.
print(dress[-3])

# Difference between Strings and Lists
# Stings only contains charters 'a', '1' '@'
# Strings are “immutable” we cannot change the contents of a string
# we must make a new string to make any change

fruit = 'Banana'
fruit[0] = 'b'  # Traceback 'str' object does not support item assignment

x = fruit.lower()  # Need to make a new string
print(x)
print(fruit)

# List are mutable x = [2,2.5,"hello", [4,5]]
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

# The in operator also works on lists
cheeses = ['Cheddar', 'Edam', 'Gouda']
print('Edam' in cheeses)
print('Brie' in cheeses)

# How long is a list?
greet = 'Hello Bob'
print(len(greet))  # based on the characters

x = [1, 2, 'joe', 99]  # based on the elements

print(len(x))  # the number of elements of any set or sequence

# The range function returns a list of numbers that range from zero to one less than the parameter
print(range(3))  # [0, 1, 2] No of elments return a list 

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))

# Traversing a list
cheeses = ['Cheddar', 'Edam', 'Gouda']
for cheese in cheeses:
    print(cheese)

empty = []
for x in empty:
    print('This never happens.')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):  # [0,1,2]
    friend = friends[i]
    print('Happy New Year:', friend)

# List Operations
# Concatenating Lists Using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

# Similarly, the * operator repeats a list a given number of times:
print([0] * 4)

w = [1, 2, 3]
print(w * 3)

# Lists Can Be Sliced Using :
# Remember: Just like in strings, the second number is “up to but not including”
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# List methods
x = list()
print(type(x))
print(dir(x))

# List Operations
# Concatenating Lists Using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

# Similarly, the * operator repeats a list a given number of times:
print([0] * 4)

w = [1, 2, 3]
print(w * 3)

# Lists Can Be Sliced Using :
# Remember: Just like in strings, the second number is “up to but not including”
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# List Methods
x = list()
print(type(x))
print(dir(x))

# Building a List from Scratch
stuff = list()
print(stuff)
stuff.append('book')
print(stuff)
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# Extend method
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

# Lists are in Orde
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

# Deleting elements
# There are several ways to delete elements from a list.
# If you know the index of the element you want, you can use pop:
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

# pop modifies the list and returns the element that was removed.
# If you don’t provide an index, it deletes and returns the last element.
t = ['a', 'b', 'c']
x = t.pop()
print(t)
print(x)

# If you don’t need the removed value, you can use the del operator:
t = ['a', 'b', 'c']
del t[1]
print(t)

# If you know the element you want to remove (but not the index), you can use remove:
t = ['a', 'b', 'c', 'b']
t.remove('b')
print(t)

# The return value from remove is None.
# To remove more than one element, you can use del with a slice index:
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

# Built-in Functions and Lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))  # Only works, when the list elements are numbers
print(sum(nums) / len(nums))

# Calcualting average using biult in functions and variables
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)  # Explict casing
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)

# Calcualting average using biult in functions and list

numlist = list()  # Created an empty list
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

# Relationship between Stings and List - They are best  friends
# A string is a sequence of characters and a list is a sequence of values, but 
# a list of characters is not the same as a string. 
# To convert from a string to a list of characters, you can use list function

s = 'spam'
t = list(s)
print(t)

# Split function breaks a string into parts and produces a list of strings.
# We think of these as words. We can access a particular word or loop through all the words.

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

# Accesing using lopps
print(stuff)
for w in stuff:
    print(w)

# Delimiter
# When you do not specify a delimiter, multiple spaces are treated like one delimiter
line = 'A lot of        Spaces'
etc = line.split()
print(etc)

# When there is no space between the characters, they are treted as a single
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

# You can specify what delimiter character to use in the splitting
line = 'first;second;third'
thing = line.split(';')
print(thing)
print(len(thing))

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)

# join is the inverse of split. It takes a list of strings and concatenates the elements.
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)

# Parsing lines or files
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)
# print(words[2])


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
