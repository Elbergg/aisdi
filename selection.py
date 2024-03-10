from random import randint


def selectionsort(list):
    # i = 0
    # smallest = min(list)
    # si = list.index(smallest)
    # list[si], list[0] = list[0], list[si]
    i = 0
    for _ in range(0, len(list)):
        smallest = list[i]
        si = i
        for n in range(i, len(list)):
            if list[n] < smallest:
                smallest = list[n]
                si = n
        list[i], list[si] = list[si], list[i]
        i += 1
    return list


if __name__ == "__main__":
    size = 50000
    list = []
    for _ in range(0, size):
        list.append(randint(0, size))
    print(selectionsort(list))
