def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


# Yeh function ek recursive function hai. Iska matlab hai:

# Function khud ko phir se call karta hai.

# Har baar jab function tri_recursion(k) call hota hai, wo k - 1 ke saath khud ko call karta hai.

# Jab k 0 ho jaata hai, tab recursion ruk jaata hai (base case).

# for example:
# tri_recursion(6)
# = 6 + tri_recursion(5)
# = 6 + (5 + tri_recursion(4))
# = 6 + (5 + (4 + tri_recursion(3)))
# = 6 + (5 + (4 + (3 + tri_recursion(2))))
# = 6 + (5 + (4 + (3 + (2 + tri_recursion(1)))))
# = 6 + (5 + (4 + (3 + (2 + (1 + tri_recursion(0))))))

# Recursion is a powerful tool in programming that allows you to solve problems by breaking them down into smaller sub-problems.

# It's like a loop that calls itself until a certain condition is met.

# But be careful with recursion, it can lead to infinite loops if not implemented correctly.

# Recursion is a powerful tool in programming that allows you to solve problems by breaking them down into smaller sub-problems.

# It's like a loop that calls itself until a certain condition is met.

# Ab result backtrack hote hue return hoga:

# tri_recursion(0) → returns 0

# tri_recursion(1) → 1 + 0 = 1, print(1)

# tri_recursion(2) → 2 + 1 = 3, print(3)

# tri_recursion(3) → 3 + 3 = 6, print(6)

# tri_recursion(4) → 4 + 6 = 10, print(10)

# tri_recursion(5) → 5 + 10 = 15, print(15)

# tri_recursion(6) → 6 + 15 = 21, print(21)
