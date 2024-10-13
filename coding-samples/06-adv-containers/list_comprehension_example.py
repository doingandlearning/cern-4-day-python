values = [1, 2, 4, 6, 8, 9]
print('values', values)

# List comprehension example
new_values = [i + 1 for i in values]
print('new_values', new_values)

list = [item + 1 for item in values if item % 2 == 0]
print('list:', list)
