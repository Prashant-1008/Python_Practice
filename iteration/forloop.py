fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

#The break Statement
fruits=["apple","banana","cherry"]
print("For loop with break")
for x in fruits:
    print(x)
    if x=="banana":
        break

#The continue Statement
fruits=["apple","banana","cherry"]
print("For loop with continue")
for x in fruits:
    if x=="banana":
        continue
    print(x)

#The range() Function
print("For loop with range")
for x in range(6):
    print(x)

#Nested Loops
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
print("Nested Loops")
for x in adj:
    for y in fruits:
        print(x,y)

#The pass Statement
print("For loop with pass")
for x in [0,1,2]:
    pass