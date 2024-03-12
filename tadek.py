from merge import mergesort, merge
from time import process_time


def load_file_into_list(file):
    final = []
    with open(file, "r") as file_handler:
        for line in file_handler.readlines():
            temp = line.split()
            for word in temp:
                final.append(word)
    return final


if __name__ == "__main__":
    list = load_file_into_list("pan_tadeusz.txt")
    end = len(list) - 1
    t1 = process_time()
    mergesort(list, 0, end)
    t2 = process_time()
    print(list)
    print(t2 - t1)
