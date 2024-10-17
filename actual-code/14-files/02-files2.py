import time

# context handler
with open("./file.txt") as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())

time.sleep(10)
print(file)