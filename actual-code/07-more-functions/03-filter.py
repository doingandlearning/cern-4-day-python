data = [1, 3, 5, 2, 7, 4, 10]


def is_even(num):
    return num % 2 == 0


even_numbers = list(filter(is_even, data))

print(even_numbers)

print(list(filter(lambda num: num % 5 == 0, data)))
