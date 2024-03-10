import random


def insertion_sort(list):
    l = len(list)
    for i in range(1, l):
        for n in range(0, i):
            if list[i] > list[n]:
                continue
            else:
                list[i], list[n] = list[n], list[i]
    return list


if __name__ == "__main__":
    size = 30000
    time = 0
    list = []
    for i in range(0, size):
        list.append(random.randint(0, size))
    print(insertion_sort(list))
