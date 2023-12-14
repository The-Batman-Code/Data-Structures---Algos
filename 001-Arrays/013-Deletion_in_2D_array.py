import numpy as np

twodarray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print(twodarray)

new2darray = np.delete(
    twodarray, 1, axis=0
)  # TC of this is O(mn) as we need to copy the remaining elements to a new array.
print(new2darray)  # SC is also O(mn) as we need more space to store the new array.
