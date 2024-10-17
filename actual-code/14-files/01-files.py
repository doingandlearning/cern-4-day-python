file = open("./file1.txt", "r")
print(file)

# .read()
# print(file.read()) # whole file as a single string!
# .readline()
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# if not file.readline():
#     print("I think you've reached the end of the file.")

# .readlines()
lines = file.readlines()
# file.seek(0)
lines = file.readlines()
lines = [line.strip() for line in lines]

for line in lines:
    print(line)
# DO SOME WORK!!


file.close()