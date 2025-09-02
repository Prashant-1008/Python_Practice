# Variables are containers for storing data values.

x=5
y="Hello"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x=4
x="Sally"
print(x)
print(type(x))
x="arjun"
print(x)
print(type(x))

# Variable Naming
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Python allows you to assign values to multiple variables in one line:
x,y,z="apple","orange","lemon"
print(x)
print(y)
print(z)

# You can assign the same value to multiple variables in one line:
x=y=z="orange"
print(x)
print(y)
print(z)

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x="awesome"
def myfunc():
    print("Python is "+x)
myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x="awesome"
def myfunc():
    x="fantastic"
    print("Python is "+x)
myfunc()
print("Python is "+x)

# The global Keyword
# Normally, when you create a variable inside a function, it is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def myfunc():
    global x
    x="fantastic"
    print("Python is "+x)
myfunc()
print("Python is "+x)

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x="fantastic"
    print("Python is "+x)