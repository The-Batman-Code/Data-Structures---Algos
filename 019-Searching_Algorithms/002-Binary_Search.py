import math


def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)

    while not (array[middle] == value) and start <= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
    print(middle)
    if array[middle] == value:
        return middle
    else:
        return -1


# TC and SC of the above method is O(logn) and O(1)


arr = [9, 8, 12, 15, 17, 19, 20, 21, 28]
binarySearch(arr, 15)
