import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    stop = time.time()
    return found, stop - start


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    stop = time.time()
    return found, stop - start


def binary_search_iterative(a_list,item):
    start = time.time()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    stop = time.time()
    return found, stop - start
    
    
def binary_search_recursive(a_list,item, start = None):
    if start is None:
        start = time.time()

    if len(a_list) == 0:
        stop = time.time()
        return False,stop - start
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            stop = time.time()
            return True, stop - start
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def time_search(search_algo,name):
    random_size = [500, 1000, 5000]
    for limit_size in random_size:
        t_seq = 0
        for x in range(100):
            randomized = get_me_random_list(limit_size)
            randomized = sorted(randomized)
            x, single_seq_search = search_algo(randomized, 999999)
            t_seq += single_seq_search

        avg_seq = t_seq / 100
        print(f"{name} took {avg_seq:10.7f} seconds to run, on average for {limit_size}")


if __name__ == "__main__":
    """Main entry point"""
    time_search(sequential_search, "Sequential search")
    time_search(ordered_sequential_search,"Ordered Sequential search")
    time_search(binary_search_iterative, "Binary search iterative")
    time_search(binary_search_recursive, "Binary search recursive")
