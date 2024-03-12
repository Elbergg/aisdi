from merge import mergesort, merge
from time import process_time


def load_file_into_list(file):
    final = []
    FUCKINGCUunt = 0
    with open(file, "r") as file_handler:
        for line in file_handler.readlines():
            temp = line.split()
            final.extend(temp)
    return final


if __name__ == "__main__":
    list = load_file_into_list("pan_tadeusz.txt")
    end = len(list) - 1
    t1 = process_time()
    print(mergesort(list, 0, end))
    t2 = process_time()
    print(t2 - t1)
