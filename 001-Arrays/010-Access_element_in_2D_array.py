import numpy as np

twodarray = np.array(
    [[1, 2, 3, 4], [5, 6, 7, 8], [0, 5, 3, 7]]
)  # TC and SC of this code is O(m*n)
print(twodarray)


def access_elements(array, rowindex, colindex):
    if rowindex >= len(array) or colindex >= len(array[0]):
        print("Invalid index")
    else:
        print(array[rowindex][colindex])


access_elements(twodarray, 1, 2)
print(twodarray[0])
print(len(twodarray))

# TC and SC both are O(1)
