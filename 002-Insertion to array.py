import array

my_array = array.array("i")  # TC = O(1) as it is just allocating memory
print(my_array)
my_array1 = array.array(
    "i", [1, 2, 3, 4, 5]
)  # TC = O(n) as it is copying n elements from here to memory
print(my_array1)
my_array1.insert(
    5, 78
)  # TC = O(n) as it is depends on the number of elements that will
# be shifted and we are taking the worst case where it is inserted at the front
print(my_array1)


# Space complexity is O(1) as needs on one space to insert the element
