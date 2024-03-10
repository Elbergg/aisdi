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
    print(insertion_sort([3, 6, 2, 8, 5, 1]))
