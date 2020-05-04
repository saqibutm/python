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

# List Constants
print([1, 2, 3])
print(['red', 'yellow', 'blue'])

print(2)

# Looking inside a list
dress = ['socks', 'shirt', 'perfume']
print(dress[2])

# list index out of range
print(dress[3])

# If an index has a negative value, it counts backward from the end of the list.
print(dress[-1])

# Difference between Strings and Lists
# Stings only contains charters 'a', '1' '@'
# Strings are “immutable” we cannot change the contents of a string
# we must make a new string to make any change

fruit = 'Banana'
fruit[0] = 'b'  # Traceback 'str' object does not support item assignment

x = fruit.lower()  # Need to make a new string
print(x)

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
