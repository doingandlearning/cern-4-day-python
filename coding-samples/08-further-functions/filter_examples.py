data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)

# Filter for even numbers using a lambda function
d1 = list(filter(lambda i: i % 2 == 0, data))
print('d1:', d1)


def is_even(i):
    return i % 2 == 0


# Filter for even numbers using a named function
d2 = list(filter(is_even, data))
print('d2:', d2)
