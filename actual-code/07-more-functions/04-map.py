data = [1,3,5, 2,7,4,10,2]

def increment(value):
    return value + 1

# Increment the values by 1
print(data)
print(list(map(lambda num: num + 1, data)))
print(list(map(increment, data)))
print(data)

new_values =[]
for value in data:
    new_values.append(increment(value))
print(new_values)