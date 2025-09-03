print('#######################################################')
print('Decorators without wrapper')
def new(func):
    print("I am new!")
    # func()
    return func

@new
def using_new():
    print("I am using new!")

using_new()

#######################################################

print('#######################################################')
print('Decorators with wrapper')
def new(func):
    def wrapper():
        print("I am new!")
        func()
    return wrapper

@new
def using_new():
    print("I am using new!")

using_new()

#######################################################

print('#######################################################')
print('Decorators with wrapper and parameters')
def new(func):
    def wrapper(name):
        print("I am new!")
        func(name)
    return wrapper

@new
def using_new(name):
    print(f"I am using new! {name}")

using_new("John")

#######################################################

print('#######################################################')
print("No wrapper decoration ")
def no_wrapper_decorator(func):
    print("Before function call")
    func()  # function ko turant call karna
    print("After function call")
    return func

@no_wrapper_decorator
def greet():
    print("Hello!")

# greet() call karne par:
greet()

#######################################################

print('#######################################################')
print("Log function call")
def log_function_call(func):
    def wrapper():
        print(f"Function {func.__name__} called")
        return func()
    return wrapper

@log_function_call
def greet():
    print("Hi there!")

greet()