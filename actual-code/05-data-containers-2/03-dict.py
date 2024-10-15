# Dictionary

new_dict = {
    "Italy": "Rome",
    "Netherlands": "Amsterdam",
    "France": "Paris"
}
print(type(new_dict))
print(new_dict)
print(new_dict.get("Italy"))
print(new_dict["Italy"])
new_dict["Italy"] = "Milan"
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())
new_dict["Switzerland"] = "Bern"
print(new_dict)

for country in new_dict:
    print(f"{new_dict[country]} is a city in {country}.")

user = {
    "name": {
        "title": "Mr",
        "first_name": "Kevin",
        "last_name": "Cunningham"
    },
    "interests": ["coding", "3d printing", "arduino"]
}
print(user["interests"][0])