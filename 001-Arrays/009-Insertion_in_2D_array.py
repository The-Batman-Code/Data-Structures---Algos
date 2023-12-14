import numpy as np

twodarray = np.array(
    [[1, 2, 3, 4], [5, 6, 7, 8], [0, 5, 3, 7]]
)  # TC and SC of this code is O(m*n)
print(twodarray)

newtwoarray = np.insert(
    twodarray, 0, [[89, 89, 89]], axis=1
)  # TC is O(nm) as we need to shift m*n elements to the right to add this. SC is O(n) or O(m) as we need to make that extra space to enter those elemets
print(newtwoarray)

# We can also use the append function to add elements to the end of a 2d array

newtwoarray = np.append(
    twodarray, [[36, 36, 36, 36]], axis=0
)  # TC and SC is O(m) or O(n) as we need to insert at the last of the 2-D array
print(newtwoarray)
