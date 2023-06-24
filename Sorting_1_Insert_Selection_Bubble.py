# The selection sort algorithm has a time complexity of O(n^2) in the worst case and O(n^2) in the average case,
# making it less efficient than other sorting algorithms such as quicksort or merge sort. However, it has the
# advantage of being simple to implement and requiring only a small amount of additional memory.
import random

def selection_sort(orig_values):
    sorted_values = orig_values[:]
    for i in range(len(sorted_values)):
        unsorted = sorted_values[i:]
        min_val = min(unsorted)
        min_index = sorted_values.index(min_val, i)
        sorted_values[min_index] = sorted_values[i]
        sorted_values[i] = min_val
        # print(values)

    return sorted_values


#   O(n^2) in the worst case.
def bubble_sort(orig_values):
    values = orig_values[:]
    while True:
        has_swapped = False
        for i in range(len(values) - 1):
            first_val = values[i]
            second_val = values[i + 1]
            # print(first_val, second_val)

            if values[i] > values[i + 1]:
                has_swapped = True
                values[i] = second_val
                values[i + 1] = first_val

        if not has_swapped:
            break

    return values


#   also O(n^2) in the worst case.
def insertion_sort(values):
    sorted_list = [values[0]]
    for i in range(1, len(values)):
        current_val = values[i]
        last_index = len(sorted_list) - 1
        print(f"i {i}, current_val {current_val}, last_index {last_index}, sorted_list, {sorted_list}")
        for k in range(last_index, -1, -1):
            if current_val > sorted_list[k]:
                sorted_list.insert(k + 1, current_val)
                break
            elif k == 0:
                sorted_list.insert(0, current_val)

    return sorted_list


# numbers = [5, 1, 9, 2, 8]
# numbers = [random.randint(1, 20) for x in range(10)]
numbers = [3, 9, 14, 19, 2, 19, 11, 13, 11, 19]
print(f"initial list {numbers}")
print(f"Selection Sort {selection_sort(numbers)}")
# print(f"Bubble Sort {bubble_sort(numbers)}")
# print(f"Insertion Sort {insertion_sort(numbers)}")
