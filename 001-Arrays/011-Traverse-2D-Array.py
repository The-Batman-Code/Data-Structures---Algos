import numpy as np

twodarray = np.array(
    [[1, 2, 3, 4], [5, 6, 7, 8], [0, 5, 3, 7]]
)  # TC and SC of this code is O(m*n)
print(twodarray)


def twodarraytraverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
        print("\n")
    return None


twodarraytraverse(twodarray)

# TC of the traverse function is O(mn) and SC is O(1) as no extra space is required to do the above operations
