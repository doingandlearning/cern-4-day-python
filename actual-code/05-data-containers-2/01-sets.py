no_longer_an_empty_set = set(("first", "second",  "third"))

# print(type(empty_set))

set1 = {"apple", "banana", "cherry", "dragonfruit"}
print(type(set1))
set1.update(["apple", "mango"])
l1 = ["one", "one", "three", "seven"]
unique =   list(set(l1))
unique.sort() #!!
print(unique)

print(len(set1))
set1.add("apple")
print(len(set1))
set1.update(["Apple", "Banana", "Cherry"], ("Apple", "banana"))
set1.remove("dragonfruit")
print(set1)
print("dragonfruit" in set1) # check for membership
