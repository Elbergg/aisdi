import random


def partition(list, p, r):
    pv = list[r]
    list[r], list[r] = list[r], list[r]
    j = p
    for i in range(p, r):
        if list[i] <= pv:
            list[j], list[i] = list[i], list[j]
            j += 1
    list[j], list[r] = list[r], list[j]
    return j


def quicksort(list, p, r):
    if p < r:
        q = partition(list, p, r)
        quicksort(list, p, q - 1)
        quicksort(list, q + 1, r)
    return list


if __name__ == "__main__":
    size = 100000
    time = 0
    list = []
    for i in range(0, size):
        list.append(random.randint(0, size))
    print(quicksort(list, 0, size - 1))
