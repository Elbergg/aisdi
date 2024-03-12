import math
import random
import time
import copy


def merge(list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = list[p + i]
    for j in range(0, n2):
        R[j] = list[q + j + 1]
    # L[n1] = float("inf")
    # R[n2] = float("inf")
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        list[k] = R[j]
        j += 1
        k += 1


def mergesort(list, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        mergesort(list, p, q)
        mergesort(list, q + 1, r)
        merge(list, p, q, r)
    return list


if __name__ == "__main__":
    size = 50000
    list = []
    for i in range(0, size):
        list.append(random.randint(0, size))
    second_list = copy.copy(list)
    start = time.time()
    mergesort(list, 0, size - 1)
    end = time.time()
    print(end - start)
    start2 = time.time()
    second_list = sorted(second_list)
    print(list)
    end2 = time.time()
    print(end2 - start2)
