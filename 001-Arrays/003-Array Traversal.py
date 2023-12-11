import array

my_array = array.array(
    "i", [1, 2, 3, 4, 5, 6]
)  # TC = O(n) as it is copying n elements from here to memory

for i in my_array:  # TC = O(n) as it is iterating through n elements in the array
    print(i)
