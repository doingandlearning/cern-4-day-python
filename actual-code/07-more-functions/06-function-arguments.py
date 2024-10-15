def log_and_run(func):
    print("I'm about to run a function")
    func()
    print("I just ran a function")

log_and_run(lambda: print("I was a function that ran"))