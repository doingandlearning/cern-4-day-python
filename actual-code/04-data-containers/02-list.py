empty_list = [1,2,3]
empty_list = list([1,2,3])

name_list = ["Dean", "Salvatore", "Marc"]

for name in name_list:
    print(name)

print(name_list[::-1])
name_list.append("Youri")
name_list.extend(["Sevgi", "Bart"])
print(name_list)
print(len(name_list))
name_list.insert(4, "Sewald")
print(name_list)
name_list.append("Kevin")
name_list.append("Kevin")
print(name_list.count("Kevin"))
name_list.remove("Kevin")
print(name_list)

while "Kevin" in name_list:
    name_list.remove("Kevin")

print(name_list.sort())
print(name_list)
print(name_list.count("Kevin"))

t1 = (1, "Matthias", 34.5)
l1 = ["Italy", "Netherlands", "England"]
t2 = (1,2,3)

nested = (t1, l1, t2)

new_value = name_list.pop()

print(new_value)
print(name_list)

while name := name_list.pop():
    print(name)
    if len(name_list) == 0:
        break

print(name_list)



