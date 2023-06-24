def quick(arr):
    if len(arr) <= 1:
        return arr[:]
    elif len(arr) == 2:
        return arr if arr[0] <= arr[1] else [arr[1], arr[0]]
    else:
        pivot = arr[-1]
        smaller = []
        greater = []

        for i in range(len(arr) - 1):
            if arr[i] <= pivot:
                smaller.append(arr[i])
            else:
                greater.append(arr[i])

        return quick(smaller) + [pivot] + quick(greater)

arranged = quick([9, 7, 5, 1, 3])
print("arranged:", arranged)
