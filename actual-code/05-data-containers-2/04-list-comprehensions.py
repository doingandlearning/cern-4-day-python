# List Comprehension
values = [2,3,4,5,6]

square_numbers = []

for value in values:
    square = value ** 2
    if square % 2 == 0:
        square_numbers.append(square)

print(square_numbers)

square_numbers_2 = [value ** 2 for value in values if value % 2 == 0]
print(square_numbers_2)
# [4, 9, 16, 25, 36]

new_dict = {}
print(new_dict.setdefault("name", "Unknown"))
print(new_dict)
print(new_dict.setdefault("name", "I know it now"))
print(new_dict)