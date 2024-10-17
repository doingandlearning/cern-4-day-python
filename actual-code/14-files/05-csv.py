import csv


with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Men in Black II", "2002", "Men in Black II"])
    writer.writerow(["The Emperor's New Groove", 2000, "Le follie dell'imperatore"])
    writer.writerow(["Corpse Bride", 2005, "La sposa cadavere"])

with open("test.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} was released in {int(row[1])} and was called {row[2]} in Italy.")