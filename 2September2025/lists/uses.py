# Uses of Python Lists — Demonstrations
# Reference: https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
# Notes:
# - Lists are ordered and mutable, allow duplicates, and can hold mixed types.
# - Common applications: data storage/manipulation, stacks/queues, iteration/data processing,
#   dynamic arrays, and string processing.

print("--- 1) Data Storage and Manipulation ---")
a = [23, 45, 12, 67, 34]
print("start:", a)
a.append(89)
print("after append 89:", a)
if 45 in a:
    a.remove(45)
print("after remove 45:", a)

print("--- 2) Implementing Stacks and Queues ---")
# Stack (LIFO)
stack = []
stack.append('a')
stack.append('b')
print("stack after pushes:", stack)
print("stack pop ->", stack.pop(), "stack now:", stack)

# Queue (FIFO) using list (note: pop(0) is O(n); prefer collections.deque in real apps)
queue = []
queue.append('first')
queue.append('second')
print("queue after enqueues:", queue)
print("queue pop(0) ->", queue.pop(0), "queue now:", queue)

print("--- 3) Iteration and Data Processing ---")
nums = [1, 2, 3, 4, 5]
print("nums:", nums)
total = sum(nums)
print("sum(nums):", total)
# simple transform
squares = [n * n for n in nums]
print("squares:", squares)

print("--- 4) Dynamic Arrays (growing while computing) ---")
s = []
for i in range(10):
    s.append(i * i)
print("squares 0..9:", s)

print("--- 5) Storing and Processing Strings ---")
sentence = "Subtle art of not giving a bug"
words = sentence.split()
print("words:", words)
for w in words:
    print("upper:", w.upper()) 