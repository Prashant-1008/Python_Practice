# List examples: creation, CRUD, stack/queue, processing

# Creation
numbers = [23, 45, 12, 67, 34]
print("numbers:", numbers)
mixed = [1, "two", 3.0, True]
print("mixed:", mixed)
empty = []  # list()
print("empty:", empty)

# CRUD operations
numbers.append(89)
print("after append 89:", numbers)
numbers.insert(1, 99)
print("after insert 99 at idx 1:", numbers)
removed_by_value = None
if 45 in numbers:
    numbers.remove(45)
    removed_by_value = 45
print("after remove 45 (if present):", numbers, "removed_by_value:", removed_by_value)
removed_last = numbers.pop()     # 89
print("after pop() ->", removed_last, "numbers:", numbers)
numbers[0] = -1
print("after set index 0 to -1:", numbers)

# Membership and length
has_34 = 34 in numbers
length = len(numbers)
print("membership has 34:", has_34, "length:", length)

# Iteration and processing
nums = [1, 2, 3, 4, 5]
print("nums for processing:", nums)
_total = sum(nums)
print("sum(nums):", _total)
squares = [n * n for n in nums]
print("squares:", squares)
odds = [n for n in nums if n % 2 == 1]
print("odds:", odds)

# Stack (LIFO)
stack = []
stack.append('a')
stack.append('b')
print("stack after pushes:", stack)
stack_top = stack.pop()  # 'b'
print("stack.pop() ->", stack_top, "stack now:", stack)

# Queue (FIFO)
queue = []
queue.append('first')
queue.append('second')
print("queue after enqueues:", queue)
queue_front = queue.pop(0)  # 'first'
print("queue.pop(0) ->", queue_front, "queue now:", queue)

# Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("matrix:", matrix)
diagonal = [matrix[i][i] for i in range(len(matrix))]
print("diagonal:", diagonal) 