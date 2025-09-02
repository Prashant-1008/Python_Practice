if 5>2:
    print("5 is greater than 2")

x=50
if x>10:
    print("x is greater than 10")

x=50
if x>10:
    print("x is greater than 10")
    if x>20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")
else:
    print("x is not greater than 10")

x=50
if x>10:
    print("x is greater than 10")

#Elif
x=50
if x>10:
    print("x is greater than 10")
elif x>20:
    print("x is greater than 20")
else:
    print("x is not greater than 10 or 20")

#Short Hand If 
if 5>2: print("5 is greater than 2")

#Short Hand If Else
print("Yes") if 5>2 else print("No")

#And
x=5
y=3
if x>y and x>0:
    print("x is greater than y and x is greater than 0")

#Or
x=5
y=3
if x>y or x>0:
    print("x is greater than y or x is greater than 0")

#Nested If
x=41
if x>10:
    print("Above ten")
    if x>20:
        print("Above twenty")
    else:
        print("Not above twenty")
else:
    print("Below ten")

#The pass Statement
x=10
if x>10:
    pass
else:
    print("x is not greater than 10")