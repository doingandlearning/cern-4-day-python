import os
print(os.getenv("PATH"))
print(os.cpu_count())
# print(os.getcwd())
# os.chdir("..")

try:
    for file in os.listdir():
        if file.endswith(".txt"):
            os.remove(file)

    os.rename("04-os.py", "04-os-changed.py")
except Exception as e:
    print("Something went wrong!")
    print(e)