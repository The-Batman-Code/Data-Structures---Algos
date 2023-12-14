import numpy as np

twodarray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print(twodarray)


def searchtwodarray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f"Element has been found at row index: {i} and column index: {j}"
    return "Element not found"


print(searchtwodarray(twodarray, 14))

# TC of the above function is O(mn) as there are two nested for loops and SC is O(1) as no extra space is required.
