# tuple

tup1 = ()
tup1 = tuple()
print(type(tup1))
tup1 = (1, 3, 5, 7)
tup1 = tuple([1,3,5,7])
print(tup1[::-1]) # reverse
print(tup1[::2]) # every second value
print(tup1[:-1])

tup2 = (1, "Kevin", True, -27.43, "Andrea")
print(tup2)

for value in tup2:
    print(value)
    if value == 1:
        print("Got 1!")
        break

if "Andrea" in tup2:
    print("Woohoo!")
else:
    print("Awh!")

nested_tuple = ("40", ("apple", "pear"), ("Albane", "Pierre"), True)

print(nested_tuple[0][0])

new_tuple = (nested_tuple, 12)
nested_tuple = (nested_tuple, 73)


