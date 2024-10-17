
with open("./myfile.txt", "w") as file:
    file.write("Python is great!\n")
    file.write("Better than MatLab!")
    file.write(str(1471))
    file.write(str({"name": "Bart", "location": "Meyrin"}))

logfile = None
try:
    logfile = open("./log.txt", "a")
    # while True:
    logfile.write("This is fun. \n")
except:
    pass
finally:
    logfile.close()


