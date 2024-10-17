class ShoppingList:
    def __init__(self, initialItems = []):
        self.items = initialItems

    def __len__(self):
        return 338238758027582

    def length_of_time(self):
        return len(self.items)

shopping_list = ShoppingList()

print(len(shopping_list))
print(shopping_list.length_of_time())

l1 = []
print(dir(shopping_list))
print(dir(l1))

print("12" / True)
