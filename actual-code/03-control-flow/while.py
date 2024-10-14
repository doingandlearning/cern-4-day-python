count = 0

while count < 10:
    print(count)
    count += 1

for num in range(10):
    print(num)
    if num > 2:
        break
else:
    print("All items were processed")