def myfunc():
    global x
    x="yesGlobal"
    print(x)
    x="noGlobal"
    print(x)
myfunc()
print(x)

print('Hello', 'World')