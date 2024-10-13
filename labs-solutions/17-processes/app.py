from multiprocessing import Pool


def factorial(num):
    if num == 0:
        return 1
    else:
        factorial_value = 1
        for i in range(1, num + 1):
            factorial_value = factorial_value * i
        return factorial_value


if __name__ == "__main__":
    # Collect results into a list and print using pool.map
    data = (5, 8, 10, 15, 3, 6, 4)
    with Pool(processes=4) as pool:
        results = pool.map(factorial, data)
        print(results)
