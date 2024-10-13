def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperatures = [12.5, 18.1, 15.6, 17.8, 20.1, 22.6, 18.9]

fahrenheit_temps = list(map(celsius_to_fahrenheit, temperatures))
print(fahrenheit_temps)

fahrenheit_temps = list(map(lambda temp: (temp * 9 / 5) + 32, temperatures))
print(fahrenheit_temps)

above_threshold = list(filter(lambda temp: temp >= 18.0, temperatures))
print(above_threshold)

results = list(
        map(lambda temp: (temp * 9 / 5) + 32,
            filter(lambda temp: temp > 14.0,
                   temperatures)))
print(results)

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

data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)

# Apply the lambda function to each element in the list
# using the map function
d1 = list(map(lambda i: i + 1, data))
print('d1', d1)


def add_one(i):
    return i + 1


# Apply the add_one function to each element in the
# list using the map function
d2 = list(map(add_one, data))
print('d2:', d2)
