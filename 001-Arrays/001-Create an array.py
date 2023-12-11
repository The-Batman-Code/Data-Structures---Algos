import array

my_array = array.array("i")  # TC = O(1) as it is just allocating memory
print(my_array)
my_array1 = array.array(
    "i", [1, 2, 3, 4, 5]
)  # TC = O(n) as it is copying n elements from here to memory
print(my_array1)

import numpy as np

np_array = np.array([], dtype=int)  # TC = O(1) as it is just allocating memory
print(np_array)
np_array1 = np.array(
    [1, 2, 3, 4, 5]
)  # TC = O(n) as it is copying n elements from here to memory
print(np_array1)


# Space complexity for just allocating memory is also O(1) as it is an empty array
# Space complexity for copying n elements from here to memory is O(n) as memory
# allocation depends on the data type and the number of elements in the array
