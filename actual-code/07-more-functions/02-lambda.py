def square(num):
    num = num + 2
    return num ** 2

# sort -> function
print(square(-3))

square = lambda num: (num + 2) ** 2
print(square(-3))

product = lambda a, b: a * b
print(product(4,5))