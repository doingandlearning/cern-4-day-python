# Example of using the random access facilities
# available with files

# Create the file
f = open('text.txt', 'w')
f.write('abcdefghijklmnopqrstuvwxyz\n')

# Now move to a specific location and write data
f.seek(10,0)
f.write('HELLO')
f.seek(6, 0)
f.write('BOO')
f.close()

with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')
