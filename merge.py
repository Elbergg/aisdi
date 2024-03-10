import math


def merge(list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(list[p + i])
    for j in range(0, n2):
        R.append(list[q + j + 1])
    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    for n in range(p, r + 1):
        if L[i] <= R[j]:
            list[n] = L[i]
            i += 1
        else:
            list[n] = R[j]
            j += 1
    return list


def mergesort(list, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        mergesort(list, p, q)
        mergesort(list, q + 1, r)
        merge(list, p, q, r)
    return list


if __name__ == "__main__":
    print(mergesort([1, 6, 3, 2, 4, 7, 9, 5], 0, 7))
