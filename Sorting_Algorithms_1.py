# The selection sort algorithm has a time complexity of O(n^2) in the worst case and O(n^2) in the average case,
# making it less efficient than other sorting algorithms such as quicksort or merge sort. However, it has the
# advantage of being simple to implement and requiring only a small amount of additional memory.

def selection_sort(orig_values):
    values = orig_values[:]
    for i in range(len(values)):
        unsorted = values[i:]
        min_val = min(unsorted)
        min_index = values.index(min_val)
        values[min_index] = values[i]
        values[i] = min_val
        # print(values)

    return values


def bubble_sort(orig_values):
    values = orig_values[:]
    while True:
        has_swapped = False
        for i in range(len(values) - 1):
            # print("started iteration with ", values)
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


def insertion_sort(values):
    sorted_list = [values[0]]
    for i in range(1, len(values)):
        current_val = values[i]
        index = len(sorted_list) - 1
        while index >= 0 and sorted_list[index] > current_val:
            index -= 1
        sorted_list.insert(index + 1, current_val)

    return sorted_list


numbers = [5, 1, 9, 2, 8]
print(f"Selection Sort {selection_sort(numbers)}")
print(f"Bubble Sort {bubble_sort(numbers)}")
print(f"Insertion Sort {insertion_sort(numbers)}")
