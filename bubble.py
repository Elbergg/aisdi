import random
from time import perf_counter


def bubblesort(list):
    start = perf_counter()
    l = len(list)
    for n in range(l - 1):
        for i in range(l - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    end = perf_counter()
    print(f"Calc time: {end-start}")
    return list, end - start


if __name__ == "__main__":
    size = 30000
    time = 0
    list = []
    for i in range(0, size):
        list.append(random.randint(0, size))
    print(bubblesort(list))
