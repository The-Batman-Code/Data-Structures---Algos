import array

my_array = array.array(
    "i", [1, 2, 3, 4, 5, 6]
)  # TC = O(n) as it is copying n elements from here to memory


def access_element(arr, ind):
    if ind >= len(arr):
        print("There is not any element in this index")
    else:
        print(arr[ind])


access_element(my_array, 2)

# Time and space complexity of this code is O(n)
