from functools import reduce

numbers = list(range(1, 11))

squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
product = reduce(lambda acc, x: acc * x, numbers, 1)

if __name__ == "__main__":
    print("numbers:", numbers)
    print("squares:", squares)
    print("evens:", evens)
    print("product 1..10:", product) 