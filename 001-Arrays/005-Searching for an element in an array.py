import array

my_array = array.array("i", [1, 2, 3, 4, 5, 6])


def linear_search(array, key):
    for i in range(
        len(array)
    ):  # TC of this code is O(n) as for loop takes n time to iterate through the array
        if array[i] == key:  # all the other functions take constant time only
            return i
    return -1


print(linear_search(my_array, 5))

# Space complexity is O(1) as we are calling this function only once which does not require extra space
