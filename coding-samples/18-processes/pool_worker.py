from multiprocessing import Pool, set_start_method


def worker(x):
    for _ in range(x * x):
        print(x, end='', flush=True)
    return x * x


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        print(pool.map(worker, [0, 1, 2, 3, 4, 5]))
