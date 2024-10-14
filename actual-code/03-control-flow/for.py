# for letter in "Python is cool":
#     print(letter)

for number in range(10):
    if number % 2 == 0:
        continue
    if number > 5:
        break
    print(number)

print("Keep doing more work down here.")