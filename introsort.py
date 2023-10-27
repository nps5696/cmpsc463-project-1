####
# Nikolay Sizov
# nps5696@psu.edu
# CMPSC 463
####

import random
import time
import matplotlib.pyplot as plt
import sys

# need for quicksort testing with deep recursion
sys.setrecursionlimit(50000)

# counter for heapsort switchover
heap_used = False
# force sorting thru quicksort
quicksort = False


def introsort(arr):
    # measure depth for switching from quicksort to heapsort
    depth = (len(arr).bit_length() - 1) * 2
    # route to next step
    introsort_router(arr, 0, len(arr), depth)


def introsort_router(arr, start, end, depth):
    # global quicksort
    # base cond., single number or lower array => nothing to sort
    if end - start <= 1:
        return
    # if depth is 0 quicksort is no longer quick->(O(n^2)), switching to heapsort
    elif depth == 0 and quicksort is False:
        global heap_used
        heap_used = True
        do_heapsort(arr, start, end)
    else:
        # let's try to sort it with quicksort
        p = partition(arr, start, end)
        introsort_router(arr, start, p + 1, depth - 1)
        introsort_router(arr, p + 1, end, depth - 1)


def do_heapsort(arr, start, end):
    do_max_heap(arr, start, end)
    for i_heap in range(end-1, start, -1):
        arr[start], arr[i_heap] = arr[i_heap], arr[start]
        do_max_heapify(arr, index=0, start=start, end=i_heap)


def do_max_heap(arr, start, end):
    def parent(i_mh):
        return (i_mh-1)//2

    length = end - start
    index = parent(length-1)
    while index >= 0:
        do_max_heapify(arr, index, start, end)
        index -= 1


def do_max_heapify(arr, index, start, end):
    def left(i_mh):
        return 2 * i_mh + 1

    def right(i_mh):
        return 2 * i_mh + 2

    size = end - start

    lt = left(index)
    rt = right(index)

    if lt < size and arr[start + 1] > arr[start + index]:
        largest = lt
    else:
        largest = index
    if rt < size and arr[start + rt] > arr[start + largest]:
        largest = rt
    if largest != index:
        arr[start + largest], arr[start + index] = arr[start + index], arr[start + largest]
        do_max_heapify(arr, largest, start, end)


def partition(array, start, end):

    # choose start element as pivot
    pivot = array[start]
    low = start + 1
    high = end - 1

    while True:
        while low <= high and array[high] >= pivot:
            high -= 1
        while low <= high and array[low] <= pivot:
            low += 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    # print("partitioned array: ", arr)
    # print("pivot index: ", low, "pivot value: ", pivot)

    # Return the position from where partition is done
    array[start], array[high] = array[high], array[start]
    # print("pivot index: ", high, "pivot value: ", pivot)
    return high


def extract_smallest(arr_e):
    print("arr_e:", arr_e)
    smallest = ()
    for i_es in range(len(arr_e)):
        if smallest == ():
            smallest = (i_es, arr_e[i_es])

        if smallest[1] > arr_e[i_es]:
            print("smallest vs current:", smallest[1], arr_e[i_es])
            smallest = (i, arr_e[i_es])

    smallest_val = arr_e.pop(smallest[0])
    print("smallest_val", smallest_val)
    return smallest_val, arr_e


# def heapsort(arr_l):
#     heap = ['' for _ in arr_l]
#     n = len(heap)
#     for i in range(0, n):
#         # print(i)
#         print("arr:", arr_l)
#         heap[i], arr_l = extract_smallest(arr)
#
#     return heap

def func_perform_graphics(data, data_qs):
    # Unpack the tuple pairs into two lists: x values and y values
    x_values, y_values = zip(*data)
    plt.scatter(x_values, y_values, color="blue", label="Intorsort")

    x_values_qs, y_values_qs = zip(*data_qs)
    plt.scatter(x_values_qs, y_values_qs, color="red",  label="Naive Quicksort")

    plt.legend(loc="upper left")

    plt.xlabel("List Length")
    plt.ylabel("Run Time")
    plt.title("Scatter Plot of Intospective Sort vs Quicksort Performance")
    plt.grid(True)
    plt.show()

# arr = [4, 10, 3, 7, 4, 6] #[12, 11, 13, 5, 6, 7]

# 11, 12, 13, 5, , 6, 7
# 11, 12, 13 ..
# 11, 5, 13, 12, ..
# 11, 5, 13, 6, 12, 7
# 11, 5, 13

# print(heapsort(arr))

# print(extract_smallest(arr))

# print(partition(arr, 0,5))


def get_list_nums():
    return [random.randint(1, 10) for _ in range(random.randint(10, 1000))]


# add list of tuples for length / time_delta records
func_performance = []
qs_func_performance = []
heap_used_counter = 0
qs_heap_used_counter = 0
num_runs = 100
# test run time
for i in range(num_runs):
    rand_arr = get_list_nums()
    start_time = time.time()
    introsort(rand_arr)
    end_time = time.time()

    if heap_used is True:
        heap_used_counter += 1
    heap_used = False

    quicksort = True
    qs_start_time = time.time()
    introsort(rand_arr)  # actually runs quicksort
    qs_end_time = time.time()

    # if heap_used == True:
    #     qs_heap_used_counter += 1
    # heap_used = False

    # exec time
    time_delta = end_time - start_time
    qs_time_delta = qs_end_time - qs_start_time
    func_performance.append((len(rand_arr), time_delta))
    qs_func_performance.append((len(rand_arr), qs_time_delta))

print("performance:", sorted(func_performance, key=lambda x: x[1], reverse=True))
print("performance:", sorted(qs_func_performance, key=lambda x: x[1], reverse=True))
print("heap_used_counter:", heap_used_counter/num_runs)
print("qs_heap_used_counter:", qs_heap_used_counter/num_runs)

func_perform_graphics(func_performance, qs_func_performance)
