import math
import time
from timeit import timeit
from random import randrange

# Globals to avoid bloating memory in case of recursive
max_value = 1_000_000
master_list = [i for i in range(max_value)]
master_list_var = master_list

def linear_search():
    master_list = list()

    # Populate master list
    try:
        while True:
            user_input = input("Populate a list ('Ctrl+C' to finish): ")
            master_list.append(user_input)
    except KeyboardInterrupt:
        print() # New line for better readability on console
        pass

    try:
        while True:
            user_input = input(f"Enter a value to search from {master_list} ('Ctrl+C' to quit): ")
            for element in master_list:
                try:
                    if str(element) == user_input:
                        print(f"{user_input} found")
                        break
                except:
                    pass
            
            print(f"{user_input} not found")
    except KeyboardInterrupt:
        pass

    print(f"{input} not found")

counter = 0
search_value = 0

def binary_search_recursive(search_value, search_list):
    size = len(search_list)
    mid = size//2
    # print(f"Max complexity for list of size {size}: {round(math.log(size), 2)}") if counter == 1 else ''
    if search_value == search_list[mid]:
        # print(f"{search_value} found after {counter} call(s)")
        search_value = 0
        return
    elif search_value < search_list[mid] and size > 1:
        binary_search_recursive(search_value, search_list[:mid])
    elif search_value > search_list[mid] and size > 1:
        binary_search_recursive(search_value, search_list[mid+1:])
    else:
        print(f"{search_value} not found after {counter} call(s)")

def binary_search_recursive_noargs():
    global counter
    global master_list_var
    global search_value

    if search_value == 0:
        search_value = randrange(max_value)

    counter += 1
    size = len(master_list_var)
    mid = size//2
    # print(f"Max complexity for list of size {size}: {round(math.log(size), 2)}") if counter == 1 else ''
    if search_value == master_list_var[mid]:
        # print(f"{search_value} found after {counter} call(s)")
        counter = 0
        master_list_var = master_list
        search_value = 0
        return
    elif search_value < master_list_var[mid] and size > 1:
        master_list_var = master_list_var[:mid]
        binary_search_recursive_noargs()
    elif search_value > master_list_var[mid] and size > 1:
        master_list_var = master_list_var[mid+1:]
        binary_search_recursive_noargs()
    else:
        print(f"{search_value} not found after {counter} call(s)")
        search_value = 0
        counter = 0

    master_list_var = master_list


def binary_search_iterative():
    global counter

    search_value = randrange(max_value)
    size = len(master_list)
    mid = size//2
    start = 0
    end = size

    print(f"Finding {search_value}")

    if search_value < master_list[start] or search_value > master_list[size-1] or size == 0:
        print(f"Search value not available. Basic check failed.")
        counter = 0
        return

    while start <= end:
        mid = (start + end) // 2
        counter += 1
        if search_value == master_list[mid]:
            # print(f"{search_value} found at location {mid} after {counter} iterations")
            counter = 0
            return
        elif search_value < master_list[mid]:
            end = mid - 1
            continue
        else:
            start = mid + 1
    
    print(f"{search_value} not found after {counter} iterations")

	
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def perf_tracker(iter_count, func, *args):
    # print(f"{func} {args}")

    total_time = 0.0
    local_counter = 0
    while local_counter < iter_count:
        start_time = time.perf_counter()
        func()
        total_time += (time.perf_counter() - start_time)
        local_counter += 1

    return round(total_time, 2)


def bubble_sort():
    unsorted_list = [randrange(1, 1_000_000, 1) for i in range(100)]
    # print(f"{unsorted_list}")
    for first in range(len(unsorted_list) - 1):
        for second in range(first + 1, len(unsorted_list)):
            if unsorted_list[first] > unsorted_list[second]:
                unsorted_list[first], unsorted_list[second] = unsorted_list[second], unsorted_list[first]

    # print(f"{unsorted_list}")

if __name__ == "__main__":
    iter_count = 1000
    # iter_time = perf_tracker(iter_count, binary_search_iterative)
    # recu_time = perf_tracker(iter_count, binary_search_recursive)
    # print(f"Time taken with iterative method for {iter_count} attempts: {iter_time}")
    # print(f"Time taken with recursive method for {iter_count} attempts: {recu_time}")
    # local_counter = 0
    # start_time = time.perf_counter()
    # while local_counter < iter_count:
    #     binary_search_recursive(randrange(max_value), master_list)
    #     local_counter += 1
    # print(f"Time taken with recursive method for {iter_count} attempts: {round(time.perf_counter() - start_time, 2)}")

    bs_time = perf_tracker(iter_count, bubble_sort)
    print(f"Time taken by bubble sort for {iter_count} attempts: {bs_time} which is on average {bs_time/iter_count}ms")