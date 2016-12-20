# Python - 2.x tutorial:
# Note: Indentation is the heart of Python Programming Language

# Variables:

int_var = 5 # Integer
print(int_var)

string_var = 'WebClub' # String
print(string_var) # can be represented as "WebClub" also

bool_var = True # Boolean
print(bool_var)

pi = 3.14 # Float
print(pi)

# Data-Type:

type(pi) # returns 'float'

type(bool_var) # returns 'bool'

# Strings:

str1 = 'web' # Strings are immutable (same as in Java).
str2 = 'club'
str = str1 + str2
print(str) # Sring Concatenation

# Indexing: Strings are indexed
str[0] # gives 'W'

# Negative Indexing:
str[-1] # gives 'b'

# Slicing of Strings:
str[0:2] # gives 'We'

len(str) # gives 7

# Lists:

list1 = [1, 4, 9, 16, 25] # Similar to arrays in 'C'
list2 = [7, 'WebClub', True, 3.14]
print(list1, list2)

# Indexing, Slicing same as in Strings

len(list1) # gives 5

list1.append('Squares')
print(list1)

list1.pop() # pops out 'Squares'
list1.pop(2) # pops out 9

# Tuples:

tuple = ('Harry', 'Potter', 15, 5) # tuples are immutable
print(tuple) # single elements can't be deleted or appended to tuples, must delete the whole tuple

del tuple # deletes the tuple

# Dictionaries:

magic = {"Harry Potter":74, "Hermoine":98, "Ron Weasley":67}
magic["Hermoine"] # gives 98

# Sets:

set = {3, 1, 4, 3, 2}
print(set) # removes duplicates

# Control Flow:

a = 1
if (a < 5):
  # do something
  print("Magic")
elif (a < 10):
  # do something
  print("Magnificant")
else:
  print("Nothing :(")
# prints 'Magic'

list = [1, 2, 3, 4, 5]
for i in list:
  print(i**2) # prints squares of the numbers in list
  
for i in range(len(list)):
  print(list[i]**2) # same as above
  
for i in range(0, 4):
  print(i) # prints 0, 1, 2, 3
  
i = 1  
while (i < 5):
  print(i)
  i = i + 1

# 'break' and 'continue' are used similar to in 'C'

# Two-Lists:

names = ['Emma', 'Regene', 'James', 'Raulph']
salary = [200, 350, 150, 400]
for i, j in zip(names, salary): # 'zip' keyword
  print(i, j)
  
# Functions:

def odd(num): # 'def' keyword
  if(num % 2 != 0):
    return True
  else:
    return False
    
odd(4) # function call - returns 'False'

# Modules:

# file.py = filename
def odd(num):
    if num%2:
       return True
    else:
       return False
       
def prime(n):
     for i in range(2,int(math.ceil(math.sqrt(n)))):
             if n%i == 0:
                return False
     return True

# Importing: (similar to #include <stdio.h>)

import file.py 
file.odd(5)

from file import odd # imports only the 'odd' function
odd(5)

from file import * # imports everything
odd(5)
prime(5)

from file import prime as function # importing 'prime' as 'function'
function(5)

# classes and file-management is 'not' discussed here

# Using Python for Data-Science:

# Use matplotlib for all the plotting purposes

# Basic plot of Population vs Year:

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, population)
plt.show()

# Scatter plot of the above graph - More convenient:

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]
plt.scatter(year, population) # function change here
plt.show()

# Histograms:

import matplotlib.pyplot as plt
help(plt.hist) # help is like the manual page
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
population = [2.519, 3.692, 5.263, 6.972]
plt.hist(values, bins = 3)
plt.show()

# Customization of Data Visualization:

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, population)
plt.fill_between(year, population, 0, color = 'blue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
['0', '2B', '4B', '6B', '8B', '10B'])
plt.show()

# while running Python code from file, use: python filename.py
