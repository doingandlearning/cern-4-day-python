def greeter(name, message = "how are you?"):
    print(f"Welcome {name} - {message}")

greeter("Bart", "Hoe is het")
greeter("Pierre", "Comment vas-tu?")
greeter("Dean")
greeter("Andrea", "Come stai?")

greeter(message="Wie geht es dir", name="Matthias")

