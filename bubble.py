import random
from time import perf_counter


def bubblesort(list):
    start = perf_counter()
    for n in range(len(list) - 1):
        for i in range(len(list) - 1):
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
        list.append(random.randint(0, 30000))
    sorted_list = bubblesort(list)
    print(bubblesort(list))
    time += list[1]
    print(f"Average calc time: {time/10}")
